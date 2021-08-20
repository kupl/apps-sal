from functools import reduce


def sum_mix(arr):
    return reduce(lambda x, y: int(x) + int(y), arr)
