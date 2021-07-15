def similarity(a, b):
    return len(set(a).intersection(set(b))) / len(set(a).union(set(b)))
