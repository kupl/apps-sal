def get_real_floor(n):
    return n if n < 1 else n - 2 if n > 13 else n - 1
