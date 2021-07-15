def merge_arrays(first, second): 
    first.extend(second)
    result = list(set(first))
    result.sort()
    return result
