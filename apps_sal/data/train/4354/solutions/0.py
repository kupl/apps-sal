def padovan(n):
    p0 = p1 = p2 = 1
    for i in range(n):
        p0, p1, p2 = p1, p2, p0 + p1
    return p0
