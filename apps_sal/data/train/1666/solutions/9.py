from fractions import gcd
from functools import reduce
solution = lambda a: reduce(gcd, a)*len(a)
