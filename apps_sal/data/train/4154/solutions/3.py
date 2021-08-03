def is_triangle(a, b, c):
    """Determine if three sides of given lengths can form a triangle.

        Args:
            a (int): First side length
            b (int): Second side length
            c (int): Third side lenght

        Returns:
            bool: True if the three sides given can form a triangle.
    """
    return a < b + c and b < a + c and c < a + b
