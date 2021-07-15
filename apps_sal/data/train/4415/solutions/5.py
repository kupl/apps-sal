from collections import Counter
from math import factorial
from operator import mul
from functools import reduce

def proc_arr(arr):
    c = Counter(arr)
    xs = sorted(arr)
    n = factorial(len(arr)) // reduce(mul, list(map(factorial, list(c.values()))))
    return [n, int(''.join(xs)), int(''.join(xs[::-1]))]

