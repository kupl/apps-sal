def merge_arrays(a, b):
    return sorted([x for x in set(a + b) if a.count(x) == b.count(x) or a.count(x) * b.count(x) == 0])
