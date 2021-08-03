def isMultiple(a, b, n):
    c = (round(a / b + 0.0001, 1) * 10) % 10
    return c % n == 0 and bool(c)
