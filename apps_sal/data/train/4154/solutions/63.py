def is_triangle(a, b, c):
    if a and b and (c > 0):
        return a + b > c and a + c > b and (b + c > a)
    else:
        return False
