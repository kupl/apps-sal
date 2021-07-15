def triple_shiftian(base,n):
    a,b,c = base
    for i in range(n):
        a, b, c = b, c, 4 * c - 5 * b + 3 * a
    return a
