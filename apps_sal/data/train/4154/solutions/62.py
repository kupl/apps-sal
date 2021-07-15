def is_triangle(a, b, c):
    #triangle inequality theorem
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

