class LCG(object):
  a = 2
  c = 3
  m = 10
  
  def __init__(self, seed):
      self.seed = seed
  
  def random(self):
      self.seed = (self.seed * self.a + self.c) % self.m
      return self.seed / 10
