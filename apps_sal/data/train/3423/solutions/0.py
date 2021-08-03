from itertools import combinations


def solve(a, n):
    return any(sum(c) % n == 0 for i in range(len(a)) for c in combinations(a, i + 1))
