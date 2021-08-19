def series_sum(n):
    return '{:.2f}'.format(round(sum((1 / (1 + e * 3) for e in range(n))), 2))
