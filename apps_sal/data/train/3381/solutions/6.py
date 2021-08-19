def get_real_floor(n):
    if n == 1:
        return 0
    elif n == 15:
        return 13
    elif n == 0:
        return 0
    elif n > 0 and n < 13:
        return n - 1
    elif n > 0 and n > 13:
        return n - 2
    else:
        return n
