def get_real_floor(n):
    return n - 1 - int(n >= 13) if n > 0 else n
