def is_triangle(a, b, c):
    if a >= 0 or b >= 0 or c >= 0:
        if a + b <= c or a + c <= b or b + c <= a:
            return False
        else:
            return True
    else:
        return False
    return False
