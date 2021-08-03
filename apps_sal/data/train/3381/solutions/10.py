def get_real_floor(n):
    if n <= 0:
        return n
    elif n < 14:
        return n - 1
    elif n == 14:
        return 12
    else:
        return n - 2
