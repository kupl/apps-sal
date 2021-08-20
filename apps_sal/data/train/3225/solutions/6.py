def find_all(array, n):
    l = []
    for (i, v) in enumerate(array):
        if v == n:
            l.append(i)
    return l
