def is_narcissistic(n):
  t = str(n)
  l = len(t)
  
  return n == sum(int(d) ** l for d in t)
