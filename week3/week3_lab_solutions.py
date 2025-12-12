"""
Week 3 Lab Solutions - REINFORCE for CartPole
Complete implementations with explanations
"""

import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
import gymnasium as gym

# TASK 1 SOLUTION: Policy Network
class PolicyNetwork(nn.Module):
    def __init__(self, state_dim=4, action_dim=2):
        super().__init__()
        hidden_dim = 32  # SOLUTION
        
        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),  # SOLUTION
            nn.Linear(hidden_dim, action_dim)
        )
    
    def forward(self, state):
        return self.network(state)
    
    # TASK 2 SOLUTION: Action Selection
    def select_action(self, state):
        state = torch.FloatTensor(state)
        logits = self.forward(state)
        
        probs = torch.softmax(logits, dim=-1)  # SOLUTION
        action = torch.multinomial(probs, 1).item()  # SOLUTION
        log_prob = torch.log(probs[action])
        
        return action, log_prob


# TASK 3 SOLUTION: Compute Returns
def compute_returns(rewards, gamma=0.99):
    """SOLUTION: Work backwards to compute discounted returns."""
    returns = []
    R = 0
    
    for r in reversed(rewards):  # SOLUTION: Iterate backwards
        R = r + gamma * R  # SOLUTION: Bellman equation
        returns.insert(0, R)  # SOLUTION: Insert at beginning
    
    return torch.FloatTensor(returns)


# TASK 4 SOLUTION: Policy Gradient Loss
def compute_policy_loss(log_probs, returns):
    """SOLUTION: Sum of -log_prob * return."""
    loss = 0
    for log_prob, G in zip(log_probs, returns):  # SOLUTION
        loss += -log_prob * G  # SOLUTION
    return loss


# Training function (uses all solutions above)
def train_reinforce(env, policy, optimizer, n_episodes=1000, gamma=0.99):
    episode_rewards = []
    
    for episode in range(n_episodes):
        log_probs = []
        rewards = []
        
        state, _ = env.reset()
        done = False
        
        while not done:
            action, log_prob = policy.select_action(state)
            next_state, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            
            log_probs.append(log_prob)
            rewards.append(reward)
            state = next_state
        
        returns = compute_returns(rewards, gamma)
        returns = (returns - returns.mean()) / (returns.std() + 1e-8)
        loss = compute_policy_loss(log_probs, returns)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        episode_rewards.append(sum(rewards))
        
        if (episode + 1) % 100 == 0:
            avg = np.mean(episode_rewards[-100:])
            print(f"Episode {episode + 1}: Avg Reward = {avg:.2f}")
    
    return episode_rewards


# TASK 5 SOLUTION: Value Baseline (Optional)
class ValueNetwork(nn.Module):
    def __init__(self, state_dim=4, hidden_dim=32):
        super().__init__()
        
        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),  # SOLUTION
            nn.ReLU(),  # SOLUTION
            nn.Linear(hidden_dim, 1)  # SOLUTION: Output 1 value
        )
    
    def forward(self, state):
        return self.network(state).squeeze()


if __name__ == "__main__":
    # Train REINFORCE
    env = gym.make('CartPole-v1')
    policy = PolicyNetwork()
    optimizer = optim.Adam(policy.parameters(), lr=0.01)
    
    print("Training REINFORCE on CartPole-v1...")
    rewards = train_reinforce(env, policy, optimizer, n_episodes=1000)
    
    print(f"\nFinal avg reward: {np.mean(rewards[-100:]):.2f}")
    
    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(rewards, alpha=0.3)
    window = 50
    ma = np.convolve(rewards, np.ones(window)/window, mode='valid')
    plt.plot(range(window-1, len(rewards)), ma, linewidth=2)
    plt.axhline(y=475, color='g', linestyle='--')
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.title('REINFORCE Training')
    plt.savefig('training_curve.png')
    print("\nSaved training curve to training_curve.png")
