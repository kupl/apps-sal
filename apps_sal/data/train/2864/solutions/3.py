def merge_arrays(a, b):
    return sorted((n for n in set(a + b) if (n in a) != (n in b) or a.count(n) == b.count(n)))
