def direction_in_grid(n, m):
    return 'UD'[m % 2] if m < n else 'LR'[n % 2]
