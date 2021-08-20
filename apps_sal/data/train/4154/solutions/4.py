def is_triangle(a, b, c):
    if a <= 0 | b <= 0 | c <= 0:
        return False
    elif a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True
