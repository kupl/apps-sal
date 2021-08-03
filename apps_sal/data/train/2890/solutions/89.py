def multiples(m, n):
    i = 0
    r = []
    while i < m:
        r.append(n * (i + 1))
        i = i + 1
    print(r)
    return r
