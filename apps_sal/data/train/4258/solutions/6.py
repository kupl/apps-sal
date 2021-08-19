def series_sum(n):
    return f'{sum((1 / d for d in range(1, n * 3, 3))):.2f}'
