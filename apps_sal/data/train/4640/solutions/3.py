from itertools import combinations


def int_diff(arr, n):
    return sum(1 for x, y in combinations(arr, 2) if abs(x - y) == n)
