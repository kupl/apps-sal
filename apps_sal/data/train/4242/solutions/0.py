def direction_in_grid(n, m):
    return 'LR'[n % 2] if m >= n else 'UD'[m % 2]
