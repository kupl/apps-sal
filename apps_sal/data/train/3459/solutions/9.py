from itertools import combinations


def solve(n, k):
    s = str(n)
    return ''.join(min(combinations(s, len(s) - k)))
