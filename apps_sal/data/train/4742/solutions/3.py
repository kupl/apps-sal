from collections import Counter


def duplicates(arr):
    return sum((v >> 1 for v in Counter(arr).values()))
