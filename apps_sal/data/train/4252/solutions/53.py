def merge_arrays(first, second): 
    a = set(first)
    b = set(second)
    return sorted(list(a|b))

