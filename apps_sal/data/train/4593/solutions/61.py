def merge_arrays(a1, a2):
    a = set(a1)
    a.update(a2) 
    return sorted(a)
