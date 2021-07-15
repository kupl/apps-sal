def hotpo(n):
    m, s = n, 0
    while m!= 1:
        if m % 2: m = 3 * m + 1
        else: m //= 2
        s += 1
    return s

