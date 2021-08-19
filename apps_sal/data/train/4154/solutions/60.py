def is_triangle(a, b, c):
    if a is 0 and b is 0 and (c is 0):
        return False
    elif a + b > c and a + c > b and (b + c > a):
        return True
    else:
        return False
