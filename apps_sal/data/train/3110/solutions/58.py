def two_decimal_places(n):
    a = 100 * n
    b = int(a)
    if a - b >= 0.5:
        d = b + 1
    elif a < 0 and b - a >= 0.5:
        d = b - 1
    else:
        d = b
    c = d / 100
    return c
