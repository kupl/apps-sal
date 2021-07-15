def get_real_floor(n):
    if 0 < n < 14:
        return n - 1
    if 13 < n:
        return n - 2
    else:
        return n
