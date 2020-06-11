# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:16:57 2020

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
deterministic = False  ## False means the agent may not go where it intends to go

class RL_Agent:

    # Define initial characteristics of agent
    
    def __init__(self):
        
        ## record states for each run
        self.states = []
        
        # how quickly the agent learns
        self.learning_rate = 0.1
        
        # the possible moves of the agent
        self.actions = ["up", "down", "left", "right"]
    
        # if agent finds a path to win state, should it stick to it?
        # define agent's willingness to explore outside of best reward state path
        self.exploration_rate = 0.5
    
        # initialise state reward values
        ## This is essentially the agent's memory - it will use this to decide it's next move every iteration (unless the agent chooses to explore)
        self.state_values = {}
        for row in range(board_rows):
            for col in range(board_columns):
                self.state_values[row, col] = 0
                
        if deterministic == True:
            self.determine = True
        else:
            self.determine = False
                
    def reset(self):
        ## bring agent back to the start of the board
        self.state = start_state
        self.states = []
    
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
            
            self.determine = False ## to ensure next move is non deterministic again
            
            return self.state # output state position if move is illegal
        
        else:
            self.action_probability()
            self.determine = True ## only necessary to confirm and record next action, agent is not deterministic
            
            
    def action_probability(self):
        ## if action
        ## process probability of action (in our case 0.8)
        ## return action intention
        ## use next state position determine to confirm next state
        
    def play(self, iterations = 10):
        
        # begin game
        i = 0
        
        while i < iterations:
        
            # check if agent has reached the end state (NEED TO DO)
            if self.state == win_state or self.state == lose_state:
                
                # begin back propagation process
                reward = self.get_reward()
                next_state_value = reward
        
                # define value iteration formula
                for s in reversed(self.states):
                    # define separate state values (estimated rewards) THIS IS CALLED VALUE ITERATION
                    self.state_values[s] = self.state_values[s] + self.learning_rate*(next_state_value - self.state_values[s]) ## new ESTIMATED state1 = old state1 + learning_rate*(new ESTIMATED state2 - old state 1)
                    next_state_value = self.state_values[s] ## assign new state1 to next_state_value for the next iteration
                # reset agent states (but not state values!)
                self.reset()
                
                # begin next iteration
                i += 1
            
            # agent is stil playing game so needs to decide next action
            else:
                # decide on action
                ## based on reward if agent chooses optimal reward path
                ## based on random choice if agent choose to explore
                action = self.choose_action()
                self.state = self.next_state_position(action) ## return new state position
                self.states.append(self.state)
    
    
    def choose_action(self):
        
        action = ""
        
        if np.random.uniform(0, 1) <= self.exploration_rate: ## can change this exploration decision later on
            # agent is going to explore
            action = np.random.choice(self.actions)
        else:
            # agent is going to stick to optimal reward path
            current_reward = 0
            for action_option in self.actions: # cycle through action options
                next_reward = self.state_values[self.next_state_position[action_option]] # check rewards of each state action
                
                if next_reward > current_reward: ## select action that presents the best reward
                    action = action_option
                    current_reward = next_reward
                
        return action
         
    def showValues(self):
        for i in range(0, BOARD_ROWS):
            print('----------------------------------')
            out = '| '
            for j in range(0, BOARD_COLS):
                out += str(self.state_values[(i, j)]).ljust(6) + ' | '
            print(out)
        print('----------------------------------')
    


if __name__ == "__main__":
    agent = RL_Agent()       
    agent.play(iterations = 30)
    agent.showValues()
                
            
            
            
            
            
            
            
            
            
            
            