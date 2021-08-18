from itertools import combinations


def solve(arr, n):
    return any(sum(x) % n == 0 for i in range(1, len(arr) + 1) for x in combinations(arr, i))
