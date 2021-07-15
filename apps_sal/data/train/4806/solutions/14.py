class LCG(object):
  a = 2
  c = 3
  m = 10
  
  def __init__(self, seed):
      self.curr = seed
  
  def random(self):
      self.curr = (LCG.a * self.curr + LCG.c) % LCG.m
      return self.curr / LCG.m
