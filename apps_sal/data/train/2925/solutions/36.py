import math

def multiply(n):
  dig_count = math.floor(math.log10(abs(n))+1) if n else 1
  return n * 5**dig_count
