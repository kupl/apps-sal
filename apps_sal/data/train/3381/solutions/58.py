def get_real_floor(n):
    if n == 0:
        return 0
    elif 13 > n > 0:
        return n - 1
    elif n > 13:
        return n - 2
    else:
        return n
