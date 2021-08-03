from scipy.special import comb as f
from functools import reduce


def transform(arr, n):
    arr = (f(x + 1, n + 1, exact=True) for x in arr)
    return reduce(lambda x, y: x ^ y, arr)
