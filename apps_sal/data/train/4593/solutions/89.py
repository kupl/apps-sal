def merge_arrays(arr1, arr2):
    new = sorted(arr1+arr2)
    return list(dict.fromkeys(new))
