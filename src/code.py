# Add code later
import matplotlib.pyplot as plt
import numpy as np

class Jackdaw:
# Jackdows and its location
  def __init__(self,loc):
    self.loc = tuple(loc)
    self.calling = False

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

                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:

                        if dr == 0 and dc == 0:
                            continue

                        r = row + dr
                        c = col + dc

                        if 0 <= r < self.n and 0 <= c < self.n:
                            self.calls[r,c] += 1
                    
                
  
