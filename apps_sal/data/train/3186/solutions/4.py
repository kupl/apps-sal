def similarity(a, b):
    a, b = set(list(a)), set(list(b))
    return len(a.intersection(b)) / len(a.union(b))
