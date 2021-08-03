def is_triangle(a, b, c):
    """The triangle is possible only when all sides are greater than 0 and
       and sum of any two sides greater than the third side.
    """
    return ((a + b) > c and (b + c) > a and (c + a) > b and a > 0 and b > 0 and c > 0)
    return False
