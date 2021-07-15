def merge_arrays(arr1, arr2):
    a = set(arr1).union(set(arr2))
    b = list(a)
    b.sort()
    return b
