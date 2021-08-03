def zeros(n):
    p = n // 5
    t = p
    while t > 0:
        t = t // 5
        p = p + t
    return p
