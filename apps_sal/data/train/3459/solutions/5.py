from itertools import combinations


def solve(n, k):
    s = str(n)
    return ''.join(min((xs for xs in combinations(s, len(s) - k))))
