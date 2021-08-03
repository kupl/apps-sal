def merge_arrays(a, b):
    i = 0
    x = []
    while len(a) > i:
        if a[i] not in x:
            x.append(a[i])
        i += 1

    i = 0
    while len(b) > i:
        if b[i] not in x:
            x.append(b[i])
        i += 1
    return sorted(x)
