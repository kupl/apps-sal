from collections import Counter
from math import gcd
from functools import reduce


def has_subpattern(string):
    cnt = list(Counter(string).values())
    v = reduce(gcd, cnt, max(cnt))
    return v != 1
