def get_real_floor(n):
    if n > 0:
        if n < 13:
            n = n - 1
        else:
            n = n - 2

    return n
