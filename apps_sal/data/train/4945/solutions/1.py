from collections import Counter


def two_by_two(animals):
    return bool(animals) and {key: 2 for key, value in Counter(animals).items() if value >= 2}
