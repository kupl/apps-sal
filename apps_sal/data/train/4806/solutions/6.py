class LCG:
  m=10
  a=2
  c=3
  def __init__(self,seed):
    self.x=seed
  def random(self):
    self.x=(self.a*self.x+self.c)%self.m
    return self.x/10
