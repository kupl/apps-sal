def merge_arrays(arr1, arr2):
    a = []
    a = list(set(arr1 + arr2))
    return sorted(a)
