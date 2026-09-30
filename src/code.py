# Add code later
import matplotlib.pyplot as plt
import numpy as np

class Jackdaw:
# Jackdows and its location
  def __init__(self,loc):
    self.loc = tuple(loc)

class Roost:
  def __init__(self,n,number_of_birds):
    #Birds need space to set down
    if not 1 <= number_of_birds <= n*n:
      raise ValueError("Msut have 1 - n*n jackdaws(number_of_birds)")

    self.n = n
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
  
