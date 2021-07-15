import math

def rounding(n,m):
  a = n - math.floor(n / m) * m
  b = math.ceil(n / m) * m - n
  return n if a == b else math.floor(n / m) * m if a < b else math.ceil(n / m) * m
