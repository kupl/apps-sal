from functools import reduce
from operator import mul
from fractions import Fraction as frac

def diagonal(n, p):
    return reduce(mul, [frac(n+1-k, k+1) for k in range(p+1)], 1)
