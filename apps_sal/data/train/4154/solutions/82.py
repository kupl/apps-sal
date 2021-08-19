def is_triangle(a, b, c):
    x = a + b
    y = b + c
    z = a + c
    if x > c and y > a and (z > b):
        return True
    else:
        return False
