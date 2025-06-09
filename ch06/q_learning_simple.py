import os, sys; sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from collections import defaultdict
import numpy as np
from common.gridworld import GridWorld
from common.utils import greedy_probs


class QLearningAgent:
    def __init__(self):
        self.gamma = 0.9
        self.alpha = 0.8
        self.epsilon = 0.1
        self.action_size = 4
        self.Q = defaultdict(lambda: 0)

    def get_action(self, state):
        if np.random.rand() < self.epsilon:  # epsilon의 확률로 무작위 행동
            return np.random.choice(self.action_size)
        else:
            qs = [self.Q[state, a] for a in range(self.action_size)]
            return np.argmax(qs)
        
    def update(self, state, action, reward, next_state, done):
        if done:
            next_q_max = 0
        else:
            next_qs = [self.Q[next_state, a] for a in range(self.action_size)]
            next_q_max = np.max(next_qs)

        target = self.gamma * next_q_max + reward
        self.Q[state, action] += (target - self.Q[state, action]) * self.alpha


if __name__ == '__main__':
    env = GridWorld()
    agent = QLearningAgent()

    episodes = 10000
    for episode in range(episodes):
        state = env.reset()

        while True:
            action = agent.get_action(state)
            next_state, reward, done = env.step(action)

            agent.update(state, action, reward, next_state, done)
            if done:
                break
            state = next_state

    env.render_q(agent.Q)