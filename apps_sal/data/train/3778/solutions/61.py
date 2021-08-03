def find_smallest_int(arr):
    res = arr[0]
    for x in arr:
        if x < res:
            res = x
    return res
