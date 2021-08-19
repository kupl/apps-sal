from collections import Counter
from functools import reduce
from math import gcd


def has_subpattern(string):
    count = Counter(string)
    n = reduce(gcd, count.values())
    return ''.join(sorted((c * (i // n) for (c, i) in count.items())))
