from operator import mul
from math import factorial
from functools import reduce
from collections import Counter

def proc_arr(arr):
    s = ''.join(sorted(arr))
    return [factorial(len(arr)) // reduce(mul, list(map(factorial, list(Counter(arr).values())))), int(s), int(s[::-1])]

