def merge_arrays(first, second): 
    st = set( first + second)
    return sorted(list(st))
