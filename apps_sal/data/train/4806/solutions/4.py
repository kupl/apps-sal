class LCG(object):
  a, c, m = 2, 3, 10
  
  def __init__(self, seed):
      self.seed = seed        # Store the seed for further use if needed one day
      self.x = seed
  
  def random(self):
      self.x = (self.a * self.x + self.c) % self.m
      return self.x / self.m
