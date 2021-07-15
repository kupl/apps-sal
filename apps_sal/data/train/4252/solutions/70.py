def merge_arrays(first, second): 
    my_set = set(first + second)
    result = list(my_set)
    result.sort()
    return result
