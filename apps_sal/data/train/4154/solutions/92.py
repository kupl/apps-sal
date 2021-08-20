def is_triangle(a, b, c):
    if a <= abs(b - c) or b <= abs(a - c) or c <= abs(a - b):
        return False
    else:
        return True
