def array_previous_less(arr):
    r = []
    for (i, x) in enumerate(arr):
        for j in range(i - 1, -1, -1):
            if arr[j] < x:
                r.append(arr[j])
                break
        else:
            r.append(-1)
    return r
