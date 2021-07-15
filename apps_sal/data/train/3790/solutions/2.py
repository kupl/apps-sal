from functools import reduce
from operator import mul
def solve(arr):
    return reduce(mul, map(len, map(set, arr)))
