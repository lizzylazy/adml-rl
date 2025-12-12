# Week 4: Deep RL with Stable-Baselines3

Learn to use professional RL libraries and compare different algorithms on LunarLander.

---

## Objectives

In this lab, you will:
1. Use stable-baselines3 to train RL agents
2. Compare different algorithms (PPO, A2C, DQN)
3. Experiment with hyperparameters and observe their effects
4. Understand what makes different algorithms work
5. (Optional) Train longer and track learning progress

---

## Lab Materials

### Lab Assignment: LunarLander
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zhaw-physical-ai/adml-rl/blob/main/week4/week4_lab_lunar_lander.ipynb)

**Tasks:**
- Task 1: Explore the LunarLander environment
- Task 2: Train your first PPO agent
- Task 3: Compare PPO, A2C, and DQN
- Task 4: Experiment with learning rates
- Task 5 (Optional): Train longer with callbacks

**Time:** ~1 hour

---

### Lab Solutions
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zhaw-physical-ai/adml-rl/blob/main/week4/week4_lab_solutions.ipynb)

Complete solutions with expected results and analysis.

---

## What You'll Learn

- **Algorithm comparison**: See PPO, A2C, DQN in action
- **Hyperparameter tuning**: Learning rate, batch size, etc.
- **Practical RL**: Using industry-standard libraries
- **Performance analysis**: Comparing different approaches

---

## Expected Results

| Algorithm | Training Steps | Mean Reward | Success |
|-----------|----------------|-------------|---------|
| PPO | 100k | 180-240 | Usually solves |
| A2C | 100k | 120-200 | More variable |
| DQN | 100k | 150-220 | Needs tuning |

**Success threshold:** 200+ average reward over 100 episodes

---

## Running Locally

All labs run in Google Colab with no setup required.

For local execution:
```bash
pip install stable-baselines3[extra] gymnasium[box2d]
```

Then open notebooks in Jupyter.

---

## Resources

- [Stable-Baselines3 Docs](https://stable-baselines3.readthedocs.io/)
- [LunarLander Environment](https://gymnasium.farama.org/environments/box2d/lunar_lander/)
- [PPO Paper](https://arxiv.org/abs/1707.06347)

