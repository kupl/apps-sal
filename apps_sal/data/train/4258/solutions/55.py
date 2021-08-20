def series_sum(n):
    a = 0
    for i in range(0, n):
        a += 1 / (1 + i * 3)
    return '{:.2f}'.format(a)
