def merge_arrays(arr1, arr2):
    temp = list(set(arr1 + arr2))
    return sorted(temp)
