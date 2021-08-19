from math import hypot, sqrt


def how_to_find_them(right_triangle):
    a = right_triangle['a'] if 'a' in right_triangle else None
    b = right_triangle['b'] if 'b' in right_triangle else None
    c = right_triangle['c'] if 'c' in right_triangle else None
    if not c:
        right_triangle['c'] = hypot(a, b)
    elif not b:
        right_triangle['b'] = sqrt(c ** 2 - a ** 2)
    else:
        right_triangle['a'] = sqrt(c ** 2 - b ** 2)
    return right_triangle
