import itertools


def sum_groups(arr):
    prev_len = 1
    while prev_len != len(arr):
        prev_len = len(arr)
        arr = [sum(g) for (k, g) in itertools.groupby(arr, key=lambda x: x % 2 == 0)]
    return len(arr)
