def series_sum(n):
    res = sum(1 / (3 * d + 1) for d in range(n))
    return f'{res:.2f}'
