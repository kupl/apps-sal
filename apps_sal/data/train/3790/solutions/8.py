from operator import mul
from functools import reduce

def solve(arr):
    return reduce(mul, (len(set(xs)) for xs in arr), 1)
