def merge_arrays(arr1, arr2):
    ar = arr1 + arr2
    ar = list(set(ar))
    ar.sort()
    return list(ar)
