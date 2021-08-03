from collections import Counter
from functools import reduce
from operator import mul


def get_num(arr):
    c = Counter(arr)
    x = reduce(mul, arr)
    d = reduce(mul, [v + 1 for v in c.values()]) - 1
    return [x, d, min(arr), x // min(arr)]
