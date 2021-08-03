def is_triangle(a, b, c):
    largest = max(a, b, c)
    return 2 * largest < a + b + c
