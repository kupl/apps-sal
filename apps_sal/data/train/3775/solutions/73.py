def digits(n):
    d = 0
    while n >= 1:
        n = n // 10
        d += 1

    return d
