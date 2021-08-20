def triangle_type(*sides):
    (a, b, c) = sorted(sides)
    if a + b <= c:
        return 0
    (ab2, c2) = (a * a + b * b, c * c)
    return 1 if ab2 > c2 else 2 if ab2 == c2 else 3
