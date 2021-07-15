from collections import Counter
from operator import floordiv
from functools import reduce
from math import factorial

def proc_arr(arr):
    count = reduce(floordiv, map(factorial, Counter(arr).values()), factorial(len(arr)))
    mini = int(''.join(sorted(arr)))
    maxi = int(''.join(sorted(arr, reverse=True)))
    return [count, mini, maxi]
