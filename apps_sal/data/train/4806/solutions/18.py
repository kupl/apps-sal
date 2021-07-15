class LCG(object):
  a = 2
  c = 3
  m = 10
  
  def __init__(self, seed):
      self.seed = seed
  
  def random(self):
        a = ((LCG.a*self.seed + LCG.c)%LCG.m)
        self.seed = a
        return a/10
