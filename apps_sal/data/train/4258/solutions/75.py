def series_sum(n):
    series = 0
    for i in range(0, n):
        series += 1 / (1 + 3 * i)
    return '{:.2f}'.format(series)
