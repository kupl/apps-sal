from collections import Counter


def majority(arr):
    c = Counter(arr).most_common(2) + [(0, 0)] * 2
    if c[0][1] != c[1][1]:
        return c[0][0]
