def digits(n):
    i = 0
    while n > 0:
        i += 1
        n = n // 10
    return i
