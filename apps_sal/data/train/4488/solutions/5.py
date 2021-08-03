from collections import Counter


def bucketize(*arr):
    r = [None] * (len(arr) + 1)
    c = Counter(arr)
    for k in sorted(c.keys()):
        v = c[k]
        if r[v]:
            r[v].append(k)
        else:
            r[v] = [k]
    return r
