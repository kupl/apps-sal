from itertools import combinations


def int_diff(arr, n):
    return sum(abs(a - b) == n for a, b in combinations(arr, 2))
