def is_triangle(a, b, c):
    return c < a + b and c > a - b and (b < a + c) and (b > a - c)
