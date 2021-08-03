from math import factorial as f
from functools import reduce
from collections import Counter
from operator import mul


def count_perms(m):
    m = sum(m, [])
    return f(len(m)) / reduce(mul, map(f, Counter(m).values()))
