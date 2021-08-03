import functools


def sum_mix(arr):
    print(arr)

    return functools.reduce(lambda x, y: int(x) + int(y), arr)
