def power_mod(x, a, n):
    ret = 1
    x = x % n
    while a:
        (a, r) = divmod(a, 2)
        if r:
            ret = ret * x % n
        x = x ** 2 % n
    return ret
