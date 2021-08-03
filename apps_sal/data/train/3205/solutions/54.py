def is_divisible(n, x, y):
    ma = n % x
    la = n % y
    ka = ma + la
    if ka == 0:
        return True
    else:
        return False
