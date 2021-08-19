def series_sum(n):
    x = 0
    y = 1
    for n in range(1, n + 1):
        x = x + y
        y = 1 / (1 / y + 3)
        n = n - 1
    return format(x, '.2f')
