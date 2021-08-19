from functools import reduce


def minimum(arr):
    #     return min(arr)
    return reduce(lambda x, y: x if x < y else y, arr)


def maximum(arr):
    #     return max(arr)
    return reduce(lambda x, y: x if x > y else y, arr)
