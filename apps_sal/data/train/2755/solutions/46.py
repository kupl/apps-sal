def multiple_of_index(arr):
    l = []
    for (i, v) in enumerate(arr):
        if i > 0 and v % i == 0:
            l.append(v)
    return l
