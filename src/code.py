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
    self.readiness = 0
    self.ready_threshold = 3
    self.vision = 1
    self.takeoff_time = None

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
        self.time = 0
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


    def step(self,grow_every=1):
        self.time += 1

        if grow_every > 0 and self.time % grow_every == 0:
            for bird in self.agents:
                if bird.calling:
                    bird.call_cells = min(bird.call_cells + 1,24)

        self.update_calls()
        self.update_takeoffs()


    def update_takeoffs_b(self,start_probility=0.01):

        recent_takeoffs = []

        for bird in self.agents:
            if bird.state == "taking_off":
                if bird.takeoff_time == self.time - 1:
                    recent_takeoffs.append(bird.loc)

        for bird in self.agents:
            if bird.state == "taking_off":
                continue

            row,col = bird.loc
            bird.readiness += self.calls[row,col]

            if bird.readiness < bird.ready_threshold:
                continue

            bird.state = "ready"

            sees_takeoff = False

            for other_row,other_col in recent_takeoffs:
                row_gap = abs(row - other_row)
                col_gap = abs(col - other_col)

                if row_gap <= bird.vision and col_gap <= bird.vision:
                    sees_takeoff = True
                    break

            if sees_takeoff or np.random.random() < start_probility:
                bird.state = "taking_off"
                bird.calling = False
                bird.takeoff_time = self.time
    
    def step_b(self,grow_every=1,start_probility=0.01):
        self.time += 1

        if grow_every > 0 and self.time % grow_every == 0:
            for bird in self.agents:
                if bird.calling:
                    bird.call_cells = min(bird.call_cells + 1,24)

        self.update_calls()
        self.update_takeoffs_b(start_probility)

        
                
  
