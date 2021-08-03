from collections import Counter
from functools import reduce
from fractions import gcd


def has_subpattern(s):
    c = Counter(s)
    m = reduce(gcd, c.values())
    return ''.join(sorted(k * (v // m) for k, v in c.items()))
