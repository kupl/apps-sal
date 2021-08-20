def triple_shiftian(base, n):
    (a, b, c) = base
    i = 0
    while i < n:
        (a, b, c) = (b, c, 4 * c - 5 * b + 3 * a)
        i += 1
    return a
