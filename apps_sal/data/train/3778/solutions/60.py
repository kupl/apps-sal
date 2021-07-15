def find_smallest_int(arr):
    st = set(arr)
    res = arr[0]
    for i in st:
        if i <= res:
            res = i
    return res
