class LCG(object):
  a = 2
  c = 3
  m = 10
  
  def __init__(self, seed):
      self.seed = seed
      self.x = self.seed
  
  def g(self):
      while True:
          self.x = (self.a*self.x + self.c) % self.m
          yield self.x
          
  def random(self):
      return next(self.g())/10
