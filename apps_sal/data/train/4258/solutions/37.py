def series_sum(n):
    return '{:.2f}'.format(sum(1.0/d for d in range(1, n*3, 3)))
