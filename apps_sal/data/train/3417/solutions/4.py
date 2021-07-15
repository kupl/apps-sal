def cut_the_ropes(arr):
    res = []
    while arr:
        res, m = res + [len(arr)], min(arr)
        arr = [l - m for l in arr if l > m]
    return res
