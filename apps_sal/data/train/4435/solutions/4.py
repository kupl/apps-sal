from functools import reduce
from math import gcd

def has_subpattern(stg):
    return reduce(gcd, set(stg.count(c) for c in set(stg)), 0) > 1
