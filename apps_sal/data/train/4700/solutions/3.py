from itertools import product
from functools import reduce


def solve(arr):
    return max(reduce(int.__mul__, p, 1) for p in product(*arr))
