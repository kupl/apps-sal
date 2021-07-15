from collections import Counter
from math import gcd
from functools import reduce
def has_subpattern(string):
    cnt = Counter(string)
    v = reduce(gcd, cnt.values())
    return ''.join(sorted(k * (n // v) for k, n in cnt.items()))
