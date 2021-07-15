def get_real_floor(n):
    if n == 0 or n == 1:
        return 0
    elif n < 0:
        return n
    elif n < 14:
        return n - 1
    else:
        return n - 2
