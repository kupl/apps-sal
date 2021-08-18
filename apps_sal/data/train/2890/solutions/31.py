def multiples(m, n):
    v = 1
    a = []
    while v <= m:
        a.append(n * v)
        v += 1
    return a
