from itertools import product
from functools import reduce
from operator import mul


def solve(A):
    return max(map(lambda g: reduce(mul, g, 1), product(*A)))
