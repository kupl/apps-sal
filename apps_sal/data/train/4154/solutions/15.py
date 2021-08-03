def is_triangle(a, b, c):
    return all([a < b + c, b < a + c, c < a + b])
