from itertools import groupby


def sum_groups(arr):
    while True:
        res = [sum(i) for _, i in groupby(arr, lambda x: x & 1)]
        if arr == res:
            return len(arr)
        arr = res
