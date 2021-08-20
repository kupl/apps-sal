def get_real_floor(n):
    return n if n <= 0 else n - 1 - int(n >= 13)
