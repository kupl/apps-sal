def thirt(n):
  seq = [1, 10, 9, 12, 3, 4]
  s = str(n)
  t = sum(seq[i%6] * int(s[-i-1]) for i in range(len(s)))
  return t if t == n else thirt(t)
