from collections import Counter


def bucketize(*arr):
    c = Counter(arr)
    c = {i: sorted([k for (k, v) in list(c.items()) if v == i]) for i in list(c.values())}
    return [c[e] if e in c else None for e in range(len(arr) + 1)]
