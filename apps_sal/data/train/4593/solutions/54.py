def merge_arrays(arr1, arr2):
    ls = list(set(arr1 + arr2))
    ls.sort()
    return ls
