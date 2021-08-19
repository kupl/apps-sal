def is_triangle(a, b, c):
    return a + b > c


def is_at_least_right(a, b, c):
    return is_triangle(a, b, c) and a * a + b * b <= c * c


def is_obtuse(a, b, c):
    return is_triangle(a, b, c) and a * a + b * b < c * c


def triangle_type(a, b, c):
    (a, b, c) = sorted([a, b, c])
    return is_triangle(a, b, c) + is_at_least_right(a, b, c) + is_obtuse(a, b, c)
