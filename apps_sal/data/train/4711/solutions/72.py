def zeros(n):
    i = 1
    x = 0
    while 5**i <= n:
        x += n // 5**i
        i += 1
    return x
