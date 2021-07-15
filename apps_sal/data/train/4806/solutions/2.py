class LCG(object):
  a = 2
  c = 3
  m = 10    
  
  def __init__(self, seed):
      self.x_n = seed
  
  def random(self):      
      # Update x_n with calculated x_n1
      self.x_n = (self.a * self.x_n + self.c) % self.m
      return self.x_n / 10
