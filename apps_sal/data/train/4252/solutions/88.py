def merge_arrays(first, second):
    res = []
    for num in first:
        if num not in res:
            res.append(num)
    for num in second:
        if num not in res:
            res.append(num)
    return sorted(res)            
   

