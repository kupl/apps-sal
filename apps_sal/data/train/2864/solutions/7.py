from collections import Counter


def merge_arrays(a, b):
    c = Counter(a)
    d = Counter(b)
    return sorted(x for x in set(a) | set(b) if c[x] == d[x] or not c[x] or not d[x])
