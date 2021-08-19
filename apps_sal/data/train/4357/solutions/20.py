def nth_smallest(arr, pos):
    res = 0
    for _ in range(pos):
        res = min(arr)
        arr.remove(min(arr))
    return res
