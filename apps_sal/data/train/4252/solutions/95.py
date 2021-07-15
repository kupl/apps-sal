def merge_arrays(first, second): 
    a = first + second
    a = list(dict.fromkeys(a))
    a.sort()
    return a
