def get_real_floor(n):
    if n > 0:
        return n - (1 + int(n >= 13))
    return n
