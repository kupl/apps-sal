def is_triangle(a, b, c):
    if a > 0 and b > 0 and (c > 0):
        if a + b > c and a + c > b and (c + b > a):
            return True
        else:
            return False
    return False
