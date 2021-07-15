def padovan(n):
  p0 = p1 = p2 = 1
  for i in range(3, n+1):
    p0, p1, p2 = p1, p2, p0+p1
  return p2
