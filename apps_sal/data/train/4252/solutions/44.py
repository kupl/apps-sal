from itertools import groupby


def merge_arrays(first, second):
    arr = first + second
    arr.sort()
    res = [i for i, j in groupby(arr)]
    return res
