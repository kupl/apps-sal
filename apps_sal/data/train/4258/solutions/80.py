def series_sum(n):
    x = 1
    s = 0
    for i in range(n):
        s += 1 / x
        x += 3
    return '{:.2f}'.format(s)
