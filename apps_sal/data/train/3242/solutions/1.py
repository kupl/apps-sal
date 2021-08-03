from operator import mul
from functools import reduce


def maximum_product(arr):
    prod_dct = {x: reduce(mul, arr[:i] + arr[i + 1:], 1) for i, x in enumerate(arr)}
    return max(arr, key=lambda x: (prod_dct[x], -x))
