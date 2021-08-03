def get_exponent(n, p):
    if int(p) <= 1:
        return None
    else:
        x = 1
        while n % (p**x) == 0:
            x += 1
    return x - 1
