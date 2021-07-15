import functools
from operator import mul
def solve(arr):
    return functools.reduce(mul, (len(set(i)) for i in arr))
