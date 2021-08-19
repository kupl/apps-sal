def rocks(n):
    r = 0
    i = 1
    while n >= 10 ** i:
        r += i * 9 * 10 ** (i - 1)
        i += 1
    r += (n - (10 ** (i - 1) - 1)) * i
    return r
