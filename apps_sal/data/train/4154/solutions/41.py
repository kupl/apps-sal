def is_triangle(a, b, c):
    # test if any combination of 2 sides is > the remaining side
    if ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
        return True

    return False
