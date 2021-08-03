from operator import mul
from functools import reduce
from collections import Counter
from math import factorial as fact


def uniq_count(s):
    return fact(len(s)) // reduce(mul, map(fact, Counter(s.lower()).values()), 1)
