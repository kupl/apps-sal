def digits(n):
    c = 0
    while n != 0:
        c += 1
        n = n // 10
    return c
