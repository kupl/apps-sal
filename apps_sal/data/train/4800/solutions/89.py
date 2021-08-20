def hotpo(n):
    c = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            c = c + 1
        else:
            n = 3 * n + 1
            c += 1
    return c
