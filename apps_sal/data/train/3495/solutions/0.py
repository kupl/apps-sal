from collections import Counter


def solve(a, b):
    return 0 if Counter(b) - Counter(a) else len(a) - len(b)
