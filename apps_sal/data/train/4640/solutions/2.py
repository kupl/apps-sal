import itertools


def int_diff(arr, n):
    return sum(abs(a - b) == n for a, b in itertools.combinations(arr, 2))
