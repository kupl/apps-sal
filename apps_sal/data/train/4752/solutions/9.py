from math import gcd
from functools import reduce


def has_subpattern(s):
    d = {k: s.count(k) for k in set(s)}
    g = reduce(gcd, d.values())
    return ''.join(sorted(k * (v // g) for k, v in d.items()))
