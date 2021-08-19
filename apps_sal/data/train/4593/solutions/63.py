def merge_arrays(arr1, arr2):
    res = arr1 + arr2
    res.sort()
    res = list(dict.fromkeys(res))
    return res
