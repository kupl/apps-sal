from collections import Counter


def group(arr):
    return [[k] * n for (k, n) in Counter(arr).items()]
