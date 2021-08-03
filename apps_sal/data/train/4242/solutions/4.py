def direction_in_grid(n, m):
    return 'LR'[n % 2] if n <= m else 'UD'[m % 2]
