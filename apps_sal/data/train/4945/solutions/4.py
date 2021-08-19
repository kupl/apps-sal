from collections import Counter


def two_by_two(a):
    return {x: 2 for (x, y) in Counter(a).items() if y > 1} if a else 0
