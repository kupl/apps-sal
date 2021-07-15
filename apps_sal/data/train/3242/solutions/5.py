from functools import reduce
from operator import mul

def maximum_product(arr):
    omit_prod = lambda i: reduce(mul, arr[:i] + arr[i + 1:])
    return sorted([(omit_prod(i), -n, n) for i, n in enumerate(arr)], reverse=True)[0][2]

