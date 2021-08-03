from collections import Counter
from functools import reduce
from math import gcd


def has_subpattern(string):
    if len(string) < 2:
        return string
    c = Counter(string)
    x = reduce(gcd, c.values())
    if x == 1:
        return ''.join(sorted(string))
    return ''.join(k * (c[k] // x) for k in sorted(c.keys()))
