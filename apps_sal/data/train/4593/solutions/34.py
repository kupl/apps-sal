def merge_arrays(arr1, arr2):
    res = []
    for num in arr1:
        if num not in res:
            res.append(num)
    for num in arr2:
        if num not in res:
            res.append(num)
    res.sort()
    return res
