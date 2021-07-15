from gmpy2 import comb
from operator import xor
from functools import reduce

transform = lambda A,x: reduce(xor, (comb(n+1, x+1) for n in A))
