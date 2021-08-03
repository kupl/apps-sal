def triple_shiftian(base, n):
    while n:
        base[0], base[1], base[2] = base[1], base[2], 4 * base[2] - 5 * base[1] + 3 * base[0]
        n -= 1
    return base[0]
