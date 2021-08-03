from functools import reduce, lru_cache
from collections import Counter
from math import factorial
from operator import mul

fact = lru_cache(maxsize=None)(factorial)


def uniq_count(s):
    return fact(len(s)) // reduce(mul, map(fact, Counter(s.upper()).values()), 1)
