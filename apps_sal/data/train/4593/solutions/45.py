def merge_arrays(arr1, arr2):
    result = list(set().union(arr1, arr2))
    result.sort()
    return result
