def merge_arrays(arr1, arr2):
    res = []
    for i in arr1 :
        if i not in res :
            res.append(i)
    for i in arr2 :
        if i not in res :
            res.append(i)
    res.sort()
    return res
