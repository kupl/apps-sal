import scipy.special as math

def rectangles(n, m):
  return int(math.comb(n,2)*math.comb(m,2))
