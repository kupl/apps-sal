from functools import reduce


def sum_mix(arr):
    return reduce(lambda x, y: x + (y if y is int else int(y)), arr, 0)
