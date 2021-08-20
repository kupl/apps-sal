from functools import reduce


def find_smallest_int(arr):
    return int(reduce(lambda x, y: y if y < x else x, arr))
