def is_triangle(a, b, c):
    return a + b + c - max(a, b, c) > max(a, b, c)
