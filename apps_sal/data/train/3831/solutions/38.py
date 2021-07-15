def angle(n):
    if n == 3:
        s = 180
    if n > 3:
        s = 180 + (n-3) * 180
    return s
