def find_smallest_int(arr):
    res = 99999999
    for i in arr:
        if i < res:
            res = i
    return res
