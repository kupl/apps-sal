def merge_arrays(first, second): 
    m = [i for i in set(first + second)]
    return sorted(m)
