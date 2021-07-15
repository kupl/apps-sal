def get_real_floor(n):
    return 0 if n == 0 or n == 1 else n - 1 if 1 < n <= 13 else n - 2 if n > 13 else n
