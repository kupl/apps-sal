from functools import reduce


def find_average(arr):
    return reduce(lambda a, b: a + b, arr) / len(arr)
