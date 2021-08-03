from functools import reduce
from operator import mul


def solve(n):
    return reduce(mul, range(n + 2, 2 * n + 1)) // reduce(mul, range(1, n + 1))
