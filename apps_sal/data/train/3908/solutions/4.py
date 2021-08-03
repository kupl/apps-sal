from collections import Counter


def solve(xs):
    fs = Counter(xs)
    return sorted(xs, key=lambda x: (-fs[x], x))
