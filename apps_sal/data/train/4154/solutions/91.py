def is_triangle(a, b, c):
    k = [a + b > c, a + c > b, b + c > a]
    return not False in k
