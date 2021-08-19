def array_change(arr):
    res = 0
    for (i, x) in enumerate(arr[1:], start=1):
        inc = max(x, 1 + max(arr[:i])) - x
        arr[i] += inc
        res += inc
    return res
