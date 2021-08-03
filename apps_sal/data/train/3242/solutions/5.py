from functools import reduce
from operator import mul


def maximum_product(arr):
    def omit_prod(i): return reduce(mul, arr[:i] + arr[i + 1:])
    return sorted([(omit_prod(i), -n, n) for i, n in enumerate(arr)], reverse=True)[0][2]
