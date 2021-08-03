def get_real_floor(n):
    if n > 13:
        return n - 2
    if n > 1 and n < 13:
        return n - 1
    if n < 0:
        return n
    else:
        return 0
