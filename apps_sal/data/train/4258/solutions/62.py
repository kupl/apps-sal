def series_sum(n):
    i = 1
    x = 0
    for a in range(n):
        x += 1 / i
        i += 3
    return '{:.2f}'.format(x)
