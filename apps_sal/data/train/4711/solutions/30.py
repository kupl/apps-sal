def zeros(n):
    t = 5
    s = 0
    while n > t:
        s += n // t
        t *= 5
    return s
