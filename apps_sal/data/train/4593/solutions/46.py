def merge_arrays(arr1, arr2):
    a = set(arr1).union(arr2)
    return sorted(list(a))
