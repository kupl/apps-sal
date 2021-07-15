from collections import Counter
from functools import reduce
from math import gcd

def has_subpattern(string):
    c = Counter(string)
    m = reduce(gcd, c.values())
    for key in c:
        c[key] //= m
    return ''.join(sorted(c.elements()))
