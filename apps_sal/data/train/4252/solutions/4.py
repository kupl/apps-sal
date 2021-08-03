def merge_arrays(first, second):
    result = list(set(first + second))
    result.sort()
    return result
