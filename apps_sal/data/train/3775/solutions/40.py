def digits(n):
    c = 0
    while n > 0:
        n = n // 10
        c = c + 1
    return c
