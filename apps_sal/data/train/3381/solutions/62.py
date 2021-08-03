def get_real_floor(n):
    if 1 <= n <= 12:
        return n - 1
    elif n <= 0:
        return n
    else:
        return n - 2
