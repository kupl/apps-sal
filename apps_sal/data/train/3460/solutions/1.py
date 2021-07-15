from collections import Counter
from functools import reduce
from math import factorial


def uniq_count(s):
    f = (factorial(c) for c in Counter(s.upper()).values())
    return factorial(len(s)) // reduce(int.__mul__, f, 1)
