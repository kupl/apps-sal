def merge_arrays(a, b):
    a.extend(b)
    return sorted(list(set(a)))
