def is_triangle(a, b, c):
    if c >= a and c >= b and a + b <= c:
        return False
    elif a >= b and a >= c and b + c <= a:
        return False
    elif b >= c and b >= a and c + a <= b:
        return False
    else:
        return True
