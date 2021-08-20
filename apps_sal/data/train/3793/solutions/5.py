def triangle_type(a, b, c):
    (c, b, a) = sorted((a, b, c))
    if a >= b + c:
        return 0
    if a * a < b * b + c * c:
        return 1
    if a * a == b * b + c * c:
        return 2
    if a * a > b * b + c * c:
        return 3
