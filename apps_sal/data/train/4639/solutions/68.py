from math import log2

def power_of_two(x):
  return 2**int(log2(x)) == x if x >= 1 else False
