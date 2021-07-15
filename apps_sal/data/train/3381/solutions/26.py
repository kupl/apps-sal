def get_real_floor(n):
    return n - [2,1][n < 13] if n > 0 else n
