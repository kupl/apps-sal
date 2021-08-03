def is_triangle(a, b, c):
    x = max(a, b, c)
    for i in a, b, c:
        if x == i and x < (a + b + c - i):
            return True

    return False
