def min_sum(arr):
    res = []
    while arr:
        res.append(max(arr)*min(arr))
        arr.remove(max(arr))
        arr.remove(min(arr))
    return sum(res)
