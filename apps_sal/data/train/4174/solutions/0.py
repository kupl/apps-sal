def smallest(n):
    x, y, m = 1, 1, 1
    while m <= n:
        if x % m == 0:
            m += 1
            y = int(x)
        else:
            x += y
    return x

