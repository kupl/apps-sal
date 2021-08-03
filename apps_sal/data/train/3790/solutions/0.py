from operator import mul
from functools import reduce


def solve(arr):
    return reduce(mul, map(len, map(set, arr)), 1)
