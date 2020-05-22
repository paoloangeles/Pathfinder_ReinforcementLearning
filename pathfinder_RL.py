# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:25:37 2020

@author: Paolo
"""

## Import required modules
import numpy as np

## Define board characteristics

board_columns = 4
board_rows = 3
start_state = [0, 0]
win_state = [3, 2]
lose_state = [3, 0]
blockade = [1, 1]
deterministic = True



# Define initial characteristics of agent

def __init__(self):
    
    # how quickly the agent learns
    self.learning_rate = 0.1
    
    # the possible moves of the agent
    self.actions = ["up", "down", "left", "right"]

    # if agent finds a path to win state, should it stick to it?
    # define agent's willingness to explore outside of best reward state path
    self.exploration_rate = 0.5

    # initialise state reward values
    self.state_values = {}
    for row in range(board_rows):
        for col in range(board_columns):
            self.state_values[row, col] = 0

## Define reward states

def get_reward(self):
    if self.state == win_state:
        return 1
    if self.state == lose_state:
        return -1
    else:
        return 0 ## i.e. have not reached end states, play on
    
    
## Define agent possible moves

def next_state_position(self, action):
    
    # define potential moves of agent
    if self.determine:
        if action == "up":
            next_state = (self.state[0] - 1, self.state[1])
        elif action == "down":
            next_state = (self.state[0] + 1, self.state[1])
        elif action == "left":
            next_state = (self.state[0], self.state[1] - 1)
        elif action == "right":
            next_state = (self.state[0], self.state[1] + 1)
        else:
            print("Illegal move made by agent")
        
        # decide if move is legal and output
        if (next_state[0] >= 0) and (next_state[0] <= 2):
            if (next_state[1] >= 0) and (next_state[0] <= 3):
                if next_state != blockade:
                    return next_state # return next state position
        
        return self.state # output state position if move is illegal
    
def play(self, iterations = 10):
    
    # begin game
    i = 0
    
    while i < iterations:
    
        # check if agent has reached the end state (NEED TO DO)
        if self.State.isEnd:
            
            # begin back propagation process
            reward = self.get_reward()
            
    
            # define value iteration formula
            for s in reversed(self.states):
                # define separate state values (estimated rewards)
                self.state_values[s] = self.state_values[s] + self.learning_rate*(reward - self.state_values[s])
            
            # reset agent states (but not state values!)
            self.reset()
            
            # begin next iteration
            i += 1
        
        # agent is stil playing game so needs to decide next action
        else:
            # decide on action based on estimated reward
            action = self.choose_action()
            self.state = self.next_state_position(action)
            


def choose_action(self):
    
    action = ""
    
    if np.random.uniform(0, 1) <= self.exploration_rate:
        # agent is going to explore
        action = np.random.choice(self.actions)
    else:
        # agent is going to stick to optimal reward path
        current_reward = 0
        for action_option in self.actions: # cycle through action options
            next_reward = self.state_values[self.next_state_position[action_option]] # check rewards of each state action
            
            if next_reward > current_reward:
                action = action_option
                current_reward = next_reward
            
    return action
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            