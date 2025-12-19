# RL Project Ideas

Choose one of these projects to work on over the next 3 sessions (6 hours total). Each project includes a working baseline and ideas for improvement.

---

## Overview

Each project provides:
- ✅ **Working baseline** - runs in 2-5 minutes
- ✅ **Colab-ready** - no setup required
- ✅ **Improvement ideas** - guided suggestions
- ✅ **Advanced extensions** - open-ended challenges
- ✅ **Can run locally** - with more compute power

**Time commitment:** 6 hours over 3 sessions
- Session 1: Run baseline, understand environment
- Session 2: Implement improvements
- Session 3: Analyze results, prepare presentation

---

## 🎮 Project 1: Atari Pong

Train an agent to play Pong using deep RL with visual inputs.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO/blob/main/projects/project1_atari_pong.ipynb)

**Domain:** Games, Computer Vision  
**Difficulty:** ⭐⭐ Easy-Medium  
**Baseline time:** ~5 minutes (100k steps)

### What You'll Learn
- CNN policies for image inputs
- Frame stacking and preprocessing
- Algorithm comparison (PPO vs DQN)
- Training on visual observations

### Quick Stats
- **State:** 84x84 grayscale images (4 frames stacked)
- **Actions:** 2 discrete (up, down)
- **Success:** 80%+ win rate vs built-in AI

[**Full README →**](project1_atari_README.md)

---

## 🚗 Project 2: Highway Driving

Train an agent for autonomous highway driving with traffic.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO/blob/main/projects/project2_highway_driving.ipynb)

**Domain:** Robotics, Autonomous Vehicles  
**Difficulty:** ⭐⭐⭐ Medium  
**Baseline time:** ~3 minutes (50k steps)

### What You'll Learn
- Safety-critical RL
- Reward shaping for safety/efficiency trade-offs
- Multi-objective optimization
- Continuous vs discrete actions

### Quick Stats
- **State:** Kinematic features (position, velocity of nearby cars)
- **Actions:** 5 discrete (idle, left, right, faster, slower)
- **Success:** 70%+ episodes without collision

[**Full README →**](project2_highway_README.md)

---

## 💰 Project 3: Stock Trading

Apply RL to algorithmic trading using real historical data.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO/blob/main/projects/project3_stock_trading.ipynb)

**Domain:** Finance, Time Series  
**Difficulty:** ⭐⭐⭐ Medium  
**Baseline time:** ~2 minutes (50k steps)

### What You'll Learn
- RL in a different domain (not games/robotics)
- Feature engineering (technical indicators)
- Risk management
- Backtesting and evaluation

### Quick Stats
- **State:** OHLC prices + position
- **Actions:** Buy, Sell, Hold
- **Success:** Outperform buy-and-hold strategy

⚠️ **Disclaimer:** Educational only, not financial advice!

[**Full README →**](project3_trading_README.md)

---

## 🤝 Project 4: Multi-Agent RL

Train multiple cooperative or competitive agents.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPO/blob/main/projects/project4_multi_agent.ipynb)

**Domain:** Multi-Agent Systems, Coordination  
**Difficulty:** ⭐⭐⭐⭐ Hard  
**Baseline time:** ~5 minutes (100k steps)

### What You'll Learn
- Coordination and communication
- Emergent behaviors
- Parameter sharing
- Cooperative vs competitive scenarios

### Quick Stats
- **Environment:** Simple Spread (3 agents, 3 landmarks)
- **Goal:** Each agent covers different landmark
- **Success:** Coordinated coverage

[**Full README →**](project4_multi_agent_README.md)

---

## 📊 Project Comparison

| Project | Domain | Difficulty | Special Features | Training Time |
|---------|--------|------------|------------------|---------------|
| 1. Pong | Games/Vision | ⭐⭐ | Visual input, classic benchmark | ~5 min |
| 2. Highway | Robotics | ⭐⭐⭐ | Safety-critical, real-world | ~3 min |
| 3. Trading | Finance | ⭐⭐⭐ | Different domain, real data | ~2 min |
| 4. Multi-Agent | Coordination | ⭐⭐⭐⭐ | Multiple agents, emergence | ~5 min |

---

## 🎯 Choosing Your Project

**Choose based on:**
- **Interest:** Pick the domain that excites you!
- **Skills:** What do you want to learn?
- **Difficulty:** How challenging do you want it?
- **Extensions:** Which has the most interesting advanced ideas?

**Can't decide?** 
- Start with **Project 1 (Pong)** - most straightforward
- Or **Project 2 (Highway)** - good balance of challenge and practicality

**Want more challenge?**
- **Project 4 (Multi-Agent)** - cutting-edge research area
- Or define your own project (discuss with instructor first)

---

## 💻 Setup

### Google Colab (Recommended)
Click any "Open in Colab" badge above. Everything runs in the browser, no setup needed!

### Local Setup
Each project has its own requirements. Generally:
```bash
pip install stable-baselines3 gymnasium
# Plus project-specific packages
```

See individual project READMEs for details.

---

## 📝 Deliverables

For your 15-minute presentation, prepare:

1. **What you did:**
   - Which project and why
   - Baseline results
   - Improvements attempted

2. **Results:**
   - Performance metrics
   - Learning curves
   - Visualizations

3. **Analysis:**
   - What worked and why
   - What didn't work
   - Interesting findings

4. **Next steps:**
   - What would you try with more time?

**No formal report required** - focus on understanding and results!

---

## 🆘 Getting Help

- **Baseline doesn't run?** Check project README troubleshooting section
- **Can't decide which project?** Ask during lab session
- **Want to try something different?** Propose your own project idea!

---

## 📚 Additional Resources

- [Stable-Baselines3 Zoo](https://github.com/DLR-RM/rl-baselines3-zoo) - Pre-trained models
- [Gymnasium Environments](https://gymnasium.farama.org/) - More environments
- [Papers with Code RL](https://paperswithcode.com/area/playing-games) - Latest research

