def get_real_floor(n):
    return 0 if n == 0 else 0 if n == 1 else n if n < 0 else n - 1 if n < 13 else n - 2
