def merge_arrays(first, second): 
    newlist = list(set(first + second))
    newlist.sort()
    return newlist
