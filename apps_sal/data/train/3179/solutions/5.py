def min_and_max(l, d, x):
  for i in range(l,d+1):
      if sum(map(int,list(str(i)))) == x:
          n = i
          break
  for i in reversed(list(range(l,d+1))):
      if sum(map(int,list(str(i)))) == x:
          m = i
          break
  return [n, m]

