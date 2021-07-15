def merge_arrays(arr1, arr2):
    arr1.extend(arr2)
    res=list(set(arr1))
    res.sort()
    return res
