def triangle_type(a, b, c):
    (a, b, c) = sorted((a, b, c))
    if a + b <= c:
        return 0
    t = a ** 2 + b ** 2 - c ** 2
    if t > 0:
        return 1
    if t == 0:
        return 2
    else:
        return 3
