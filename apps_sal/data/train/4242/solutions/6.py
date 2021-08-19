def direction_in_grid(n, m):
    return 'LRUD'[min(n, m) % 2 + 2 * (m < n)]
