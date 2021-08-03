def similarity(a, b):
    a, b = set(tuple(a)), set(tuple(b))
    return len(a.intersection(b)) / len(a.union(b))
