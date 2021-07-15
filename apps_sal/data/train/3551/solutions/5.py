def array_previous_less(arr):
    r = []
    for i, v in enumerate(arr):
        x = -1
        for w in arr[:i]:
            if w < v:
                x = w
        r.append(x)
    return r
