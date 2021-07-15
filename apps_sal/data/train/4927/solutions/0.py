from functools import reduce
from gmpy2 import comb
from operator import xor

def transform(a, x):
    return reduce(xor, (comb(n + 1, x + 1) for n in a))
