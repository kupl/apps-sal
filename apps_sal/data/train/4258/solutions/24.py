def series_sum(n):
    return '%0.2f' % round(sum([1 / (1 + (x - 1) * 3) for x in range(1, n + 1)]), 2)
