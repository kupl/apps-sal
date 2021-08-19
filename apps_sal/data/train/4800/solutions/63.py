def hotpo(n):
    c = 0
    while n != 1:
        (d, r) = divmod(n, 2)
        if r is 0:
            n = d
        else:
            n = 3 * n + 1
        c += 1
    return c
