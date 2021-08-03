def is_triangle(a, b, c):
    if 2 * max([a, b, c]) < a + b + c:
        return True
    else:
        return False
