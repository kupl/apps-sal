from collections import Counter
from functools import reduce
from math import gcd


def has_subpattern(string):
    return reduce(gcd, Counter(string).values()) > 1
