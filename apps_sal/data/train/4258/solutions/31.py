def series_sum(n):
    return format(sum(1/(1+3*k) for k in range(n)),'.2f')
