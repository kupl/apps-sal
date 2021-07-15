def is_triangle(a, b, c):
    if a + b + c == 0:
        return False
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True
