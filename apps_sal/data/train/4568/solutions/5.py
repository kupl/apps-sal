from functools import reduce
from fractions import Fraction


def index(l, x, f):
    return f((i for (i, v) in enumerate(l) if (v > 0) == (x > 0)), default=None)


def find_min_max_product(arr, k):
    if k > len(arr):
        return None
    if len(arr) == 1:
        return (arr[0], arr[0])
    arr = sorted(arr, key=lambda n: (abs(n), -n))
    prod = reduce(lambda a, b: a * b, arr[-k:], 1)
    if all(((n > 0) == (arr[0] > 0) for n in arr)):
        return tuple(sorted([reduce(lambda a, b: a * b, arr[-k:], 1), reduce(lambda a, b: a * b, arr[:k], 1)]))
    if min(k, len(arr) - k) == 0:
        return (prod, prod)
    (ln, le, rn, re) = [index(arr[:-k], 1, max), index(arr[:-k], -1, max), index(arr[-k:], 1, min), index(arr[-k:], -1, min)]
    try:
        antiprod = int(prod * min([Fraction(arr[l], arr[r - k]) for (l, r) in [(le, rn), (ln, re)] if None not in (l, r)], default=prod // next((n for n in arr[:-k] if n != 0))))
    except:
        antiprod = 0
    return tuple(sorted([prod, antiprod]))
