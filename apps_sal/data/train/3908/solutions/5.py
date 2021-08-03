from collections import Counter


def solve(arr):
    c = Counter(arr)
    return sorted(arr, key=lambda x: (-c[x], x))
