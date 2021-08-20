def is_triangle(a, b, c):
    if c >= a and c >= b and (a + b > c):
        return True
    elif a >= b and a >= c and (b + c > a):
        return True
    elif b >= a and b >= c and (a + c > b):
        return True
    else:
        return False
