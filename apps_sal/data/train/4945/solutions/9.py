from collections import Counter


def two_by_two(animals):
    return bool(animals) and dict(((k, 2) for (k, v) in Counter(animals).items() if v >= 2))
