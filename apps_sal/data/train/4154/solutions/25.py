def is_triangle(a, b, c):
    # All you have to do is use the Triangle Inequality Theorem.
    return (a + b) > c and (a + c) > b and (b + c) > a
