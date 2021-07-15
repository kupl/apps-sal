def Guess_it(n,m):
  result = []
  delta = n*5 - m
  for idx, i in enumerate(range(n-delta, int(1+n-delta/2))):
      if i>=0:
          result.append([i, delta-2*idx, idx])
  return result
