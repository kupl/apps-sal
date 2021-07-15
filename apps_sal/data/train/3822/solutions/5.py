import itertools


def pair_zeros(arr):
    it = itertools.count(1)
    return [x for x in arr if x > 0 or next(it) % 2]
