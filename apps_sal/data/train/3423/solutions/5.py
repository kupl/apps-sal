from itertools import combinations


def solve(arr, n):
    return any((sum(c) % n == 0 for i in range(1, len(arr) + 1) for c in combinations(arr, i)))
