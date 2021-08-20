def array_change(arr):
    (m, s) = (0, arr[0])
    for i in arr[1:]:
        if s >= i:
            s += 1
            m += s - i
        else:
            s = i
    return m
