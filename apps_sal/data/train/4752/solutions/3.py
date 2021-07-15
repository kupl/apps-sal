from collections import Counter as C
from functools import reduce as R
from fractions import gcd


def has_subpattern(s):
    c = C(s)
    a = R(gcd, c.values())
    return "".join(sorted([x * int(c[x] / a) for x in c]))
