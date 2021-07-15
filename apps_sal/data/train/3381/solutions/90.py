def get_real_floor(n):
    if 1 <= n <= 13:
        return n - 1
    elif n >= 14:
        return n - 2
    else:
        return n
