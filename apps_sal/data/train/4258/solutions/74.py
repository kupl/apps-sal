def series_sum(n):
    sum = 0.0
    denom = 1.0
    for i in range(1, n + 1):
        sum = sum + 1 / denom
        denom = denom + 3.0
    return f'{sum:.2f}'
