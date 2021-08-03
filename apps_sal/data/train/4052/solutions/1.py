from collections import Counter
from functools import reduce
from operator import mul


def get_num(arr):
    n, small = reduce(mul, arr), min(arr)
    count = reduce(mul, (v + 1 for v in Counter(arr).values())) - 1
    return [n, count, small, n // small]
