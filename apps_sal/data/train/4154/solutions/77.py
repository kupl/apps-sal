def is_triangle(a, b, c):
    """Return boolean True if a triangle can be built with 3 given sides, else return False."""
    return True if (a + b) > c and (a + c) > b and (b + c) > a else False
