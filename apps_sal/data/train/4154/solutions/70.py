def is_triangle(a, b, c):
    if (abs(a - b) < c) and (abs(b - c) < a) and (abs(a - c) < b):
        return True
    return False
