def is_triangle(a, b, c):
    result = ''
    if a + b <= c:
        result = False
    elif a + c <= b:
        result = False
    elif b + c <= a:
        result = False
    else:
        result = True
    return result
