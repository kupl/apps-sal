def merge_arrays(first, second): 
    th = first + second
    th = list(set(th))
    th.sort()
    return th
