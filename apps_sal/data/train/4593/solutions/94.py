def merge_arrays(arr1, arr2):
    x = arr1 + arr2
    return sorted([i for i in set(x)])
