def is_triangle(a, b, c):
    """
    The sum of any two sides must be greater than the length of the third side
    """
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
