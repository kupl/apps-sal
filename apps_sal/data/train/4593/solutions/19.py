def merge_arrays(arr1, arr2):
    arr1 = arr1 + arr2
    res = []
    for i in arr1:
        if i not in res:
            res.append(i)
    return sorted(res)
