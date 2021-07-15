def climb(n):
  res = [n]
  while res[-1] != 1: res.append(res[-1]//2)
  return res[::-1]
