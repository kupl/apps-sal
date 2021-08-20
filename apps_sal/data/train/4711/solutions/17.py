def zeros(n):
    (i, j) = (1, 0)
    while 5 ** i <= n:
        (i, j) = (i + 1, j + int(n / 5 ** i))
    return j
