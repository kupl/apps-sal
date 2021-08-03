def merge_arrays(first, second):
    a = list(set(first))
    b = list(set(second))
    return sorted(list(set(a + b)))
