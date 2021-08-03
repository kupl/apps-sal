from collections import Counter


def solve(arr):
    return sum(arr) / Counter(arr).most_common(1)[0][1]
