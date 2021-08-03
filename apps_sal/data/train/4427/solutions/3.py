from itertools import groupby


def sum_groups(arr):
    reduced = [sum(gp) for _, gp in groupby(arr, key=lambda x: x % 2)]
    return len(reduced) if reduced == arr else sum_groups(reduced)
