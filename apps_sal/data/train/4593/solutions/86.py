def merge_arrays(arr1, arr2):
    concat_set = list(set(arr1 + arr2))
    concat_set.sort()
    return concat_set
