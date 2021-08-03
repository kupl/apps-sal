from collections import Counter
from functools import reduce
from math import factorial


def uniq_count(s):
    return factorial(len(s)) // reduce(lambda x, y: factorial(y) * x, list(Counter(s.lower()).values()), 1)
