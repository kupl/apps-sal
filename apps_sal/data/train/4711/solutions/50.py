def zeros(n):
    x = 0
    z = 5
    while n > 0:
        n /= 5
        x += int(n)
    return x
