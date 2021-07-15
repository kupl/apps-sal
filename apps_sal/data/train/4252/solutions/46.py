def merge_arrays(first, second): 
    x = sorted(first + second)
    return list(dict.fromkeys(x))
