from collections import Counter
from bisect import insort


def bucketize(*arr):
    c = Counter(arr)
    xs = [None] * (len(arr) + 1)
    for key, cnt in c.items():
        if xs[cnt] is None:
            xs[cnt] = []
        insort(xs[cnt], key)
    return xs
