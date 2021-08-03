from itertools import product
from functools import reduce


def solve(arr):
    return max(reduce(lambda m, n: m * n, prod) for prod in product(*arr))
