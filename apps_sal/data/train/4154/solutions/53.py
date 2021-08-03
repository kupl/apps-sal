def is_triangle(a, b, c):
    sum = a + b + c
    for side in a, b, c:
        if sum - side <= side:
            return False
    return True
