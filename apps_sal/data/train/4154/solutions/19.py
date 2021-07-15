def is_triangle(a, b, c):
    s = a + b + c
    if s - max(a,b,c) > max(a,b,c):
        return True
    return False
