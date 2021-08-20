def get_real_floor(n):
    return [n, n - [2, 1][n < 13]][n > 0]
