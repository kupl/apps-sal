def merge_arrays(first, second): 
    first.extend(second)
    first=list(set(first))
    return sorted(first)
