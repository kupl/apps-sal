def is_triangle(a, b, c):
    # Triangle inequality
    return a + b > c and a + c > b and b + c > a
