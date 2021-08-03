from functools import reduce
from operator import mul


def maximum_product(arr):
    l = [(reduce(mul, arr[:i] + arr[i + 1:]), j) for i, j in enumerate(arr)]
    return max(l, key=lambda x: (x[0], -x[1]))[1]
