# -*- coding: utf-8 -*-
"""
Created on Tue May 19 10:25:37 2020

@author: Paolo
"""


## Define board characteristics

board_columns = 4
board_rows = 3
start_state = [0, 0]
win_state = [3, 2]
lose_state = [3, 0]
blockade = [1, 1]
deterministic = True


## Define reward states

def get_reward(self):
    if self.state == win_state:
        return 1
    if self.state == lose_state:
        return -1
    else:
        return 0 ## i.e. have not reached end states, play on
    
    
## Define agent possible moves

def next_state_move(self, action):
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
        
        # if move is legal
        if (next_state[0] >= 0) and (next_state[0] <= 2):
            if (next_state[1] >= 0) and (next_state[0] <= 3):
                if next_state != blockade:
                    return next_state
        
        return self.state # if move is illegal