def snail(column, d, n):
    k = 1
    v = d
    while v < column:
        v -= n
        v += d
        k += 1
    return k
