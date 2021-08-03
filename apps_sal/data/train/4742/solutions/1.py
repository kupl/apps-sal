from collections import Counter


def duplicates(arr):
    return sum(v // 2 for v in list(Counter(arr).values()))
