def get_real_floor(n):
    return n - 1 + (n <= 0) - (n > 13)
