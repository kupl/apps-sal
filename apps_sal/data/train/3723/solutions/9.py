def array_change(arr):
    p, r = arr[0], 0
    for x in arr[1:]:
        if x <= p:
            r += p - x + 1
            x = p + 1
        p = x
    return r
