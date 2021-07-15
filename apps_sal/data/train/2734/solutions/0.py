from itertools import combinations
from math import hypot

def peaceful_yard(yard, d):
  cats = ((i, j) for i,r in enumerate(yard) for j,c in enumerate(r) if c in 'LMR')
  return all(hypot(q[0] - p[0], q[1] - p[1]) >= d for p,q in combinations(cats, 2))
