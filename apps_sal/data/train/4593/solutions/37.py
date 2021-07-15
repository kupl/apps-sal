def merge_arrays(arr1, arr2):
    print(arr1 + arr2)
    res = list(arr1 + arr2)
    res = sorted(set(res))
    return res
