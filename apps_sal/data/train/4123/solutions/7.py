from math import gcd, sqrt, ceil
from itertools import chain

def lcm(x, y): return x // gcd(x, y) * y

def lcm_cardinality(n):
  root    = ceil(sqrt(n))
  divisor = chain.from_iterable([i, n // i] for i in range(1, root) if n % i == 0)
  divisor = list(chain([root] if root * root == n else [], divisor))
  size    = len(divisor)
  return sum(1 for i in range(size) for j in range(i, size) if lcm(divisor[i], divisor[j]) == n)
