def is_triangle(a, b, c):
    if a > 0 and b > 0 and (c > 0):
        if a + b > c and b + c > a and (a + c > b):
            return True
        elif a == b == c:
            return True
        else:
            return False
    else:
        return False
