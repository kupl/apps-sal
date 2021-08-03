def series_sum(n):
    sum = 0.00
    denom = 1.00
    for i in range(1, n + 1):
        sum = sum + 1 / denom
        denom = denom + 3.00

    return f'{sum:.2f}'
