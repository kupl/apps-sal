def get_real_floor(n):
    if n < 1:
        return n
    return n - 2 if n > 13 else n - 1
