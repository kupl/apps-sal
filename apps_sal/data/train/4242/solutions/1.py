def direction_in_grid(n, m):
    return 'LRUD'[n % 2 if m >= n else 2 + m % 2]
