def array_previous_less(a):
    r = []
    for i, x in enumerate(a):
        for j in range(i - 1, -1, -1):
            if a[j] < x:
                r.append(a[j])
                break
        else:
            r.append(-1)
    return r
