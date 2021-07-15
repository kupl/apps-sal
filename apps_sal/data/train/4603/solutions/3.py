def val(v):
  return isinstance(v, int) and v >= 0

def Ackermann(m, n):
  if not val(m) or not val(n): return None
  if m == 0: return n + 1
  elif m > 0 and n == 0: return Ackermann(m - 1, 1)
  return Ackermann(m - 1, Ackermann(m, n - 1))
