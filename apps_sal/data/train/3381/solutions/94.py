def get_real_floor(n):
    if 0 < n <= 13:
        n = n - 1
    elif n > 13:
        n = n - 2
    return n
