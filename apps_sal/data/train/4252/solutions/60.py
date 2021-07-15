def merge_arrays(first, second): 
    first.extend(second)
    sett = set(first)
    arr = list(sett)
    arr.sort()
    return arr
