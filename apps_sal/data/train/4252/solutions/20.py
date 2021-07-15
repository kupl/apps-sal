def merge_arrays(first, second): 
    res = first + second
    res = list(dict.fromkeys(res))
    res.sort()
    return res
