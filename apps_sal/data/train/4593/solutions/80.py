def merge_arrays(arr1, arr2):
    arr1.extend(arr2)
    arr1=list(set(arr1))
    return sorted(arr1)
