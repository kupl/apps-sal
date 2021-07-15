def mormons(n, r, target):
    c = 0
    while n < target:
        n *= r + 1
        c += 1
    return c
