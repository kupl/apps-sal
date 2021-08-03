from collections import Counter
from functools import reduce
from math import gcd


def has_subpattern(s):
    return reduce(gcd, Counter(s).values()) > 1
