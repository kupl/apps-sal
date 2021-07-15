def is_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (c + a > b) and (a > 0) and (b > 0) and (c > 0):
        return True
    else:
        return False

