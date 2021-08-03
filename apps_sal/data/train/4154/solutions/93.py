def is_triangle(a, b, c):
    return a > abs(b - c) and b > abs(a - c) and c > abs(a - b)
