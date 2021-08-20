from itertools import groupby


def sum_groups(arr):
    while True:
        n = len(arr)
        arr = [sum(grp) for (key, grp) in groupby(arr, key=lambda x: x % 2)]
        if len(arr) == n:
            return n
