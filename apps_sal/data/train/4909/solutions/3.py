class Random():
  def __init__(self, seed):
    self.seed = (seed if seed else 0x12345678) & 0xffffffff
  def randint(self, start, end):
    return int(self.random()*(end - start + 1) + start)
  def random(self): # xorshift
    x = self.seed
    x ^= (x << 13) & 0xffffffff
    x ^= (x >> 17)
    x ^= (x <<  5) & 0xffffffff
    self.seed = x
    return x/(1 << 32)
