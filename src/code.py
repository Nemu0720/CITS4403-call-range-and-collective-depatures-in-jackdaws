# Add code later
import matplotlib.pyplot as plt
import numpy as np

class Jackdaw:
# Jackdows and its location
  def __init__(self,loc):
    self.loc = tuple(loc)
    self.calling = False
    self.call_cells = 8
    self.threshold = 1
    self.state = "roosting"

    inner = []
    outer = []

    for dr in range(-2,3):
        for dc in range(-2,3):
            if dr == 0 and dc == 0:
                continue

            if abs(dr) <= 1 and abs(dc) <= 1:
                inner.append((dr,dc))
            else:
                outer.append((dr,dc))

    np.random.shuffle(outer)
    self.call_offsets = inner + outer

            

class Roost:
    
    def __init__(self,n,number_of_birds):
        #Birds need space to set down
        if not 1 <= number_of_birds <= n*n:
          raise ValueError("Msut have 1 - n*n jackdaws(number_of_birds)")

        self.n = n
        self.calls = np.zeros((n,n),dtype=int)
        locs = []
        for row in range(n):
          for col in range(n):
            locs.append((row,col))

        np.random.shuffle(locs)
    
        self.agents = []
        for i in range(number_of_birds):
          loc = locs[i]
          bird = Jackdaw(loc)
          self.agents.append(bird)

    def update_calls(self):
        self.calls.fill(0)

        for bird in self.agents:
            if bird.calling:
                row, col = bird.loc

                for i in range(bird.call_cells):
                    dr, dc = bird.call_offsets[i]
                    
                    r = row + dr
                    c = col + dc

                    if 0 <= r < self.n and 0 <= c < self.n:
                        self.calls[r,c] += 1

    def update_takeoffs(self):
        for bird in self.agents:
            if bird.state == "roosting":
                row, col = bird.loc
                singal = self.calls[row,col]

                if singal >= bird.threshold:
                    bird.state = "taking_off"
                    bird.calling = False
                
  
