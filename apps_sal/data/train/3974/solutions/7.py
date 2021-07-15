def two_count(n):
  n = bin(n)[2:]
  
  return len(n) - len(n.strip('0'))

