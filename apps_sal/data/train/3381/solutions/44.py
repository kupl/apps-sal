def get_real_floor(n):
    return n - 1 - (n > 12) + (n <= 0)
