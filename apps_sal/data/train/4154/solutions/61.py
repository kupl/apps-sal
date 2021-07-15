def is_triangle(a, b, c):
    if a and b and c > 0 and ((a + c > b) and (b + a > c) and (c + b > a)):
        return True
    else:
        return False

