def swap_head_tail(arr):
    if len(arr) == 1:
        return arr
    n = len(arr) // 2
    (res, res2) = (arr[:n], arr[-n:])
    if len(arr) % 2 == 1:
        res.insert(0, arr[n])
    return res2 + res
