def series_sum(n):
    n = n - 1
    return f'{sum(1/i for i in range(1,2+3*n,3)):.2f}'
