def merge_arrays(arr1, arr2):
    temp = arr1 + arr2
    res = [] 
    for i in temp: 
        if i not in res: 
            res.append(i)
    res.sort()
    return res
