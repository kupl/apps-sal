def series_sum(n):
    return '{:.2f}'.format(sum(1.0 / (3 * i + 1) for i in range(n)))
