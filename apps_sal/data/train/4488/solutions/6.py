from collections import Counter


def bucketize(*args):
    r = [None] * (len(args) + 1)
    for (x, y) in sorted(Counter(args).items()):
        if r[y] is None:
            r[y] = []
        r[y].append(x)
    return r
