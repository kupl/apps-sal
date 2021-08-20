def get_real_floor(n):
    if n < 13:
        if n < 0:
            o = n
        elif n == 0:
            o = 0
        else:
            o = n - 1
    elif n == 13:
        o = 0
    else:
        o = n - 2
    return o
