def is_triangle(a, b, c):
    a = sorted([a, b, c])
    return a[2] < a[0] + a[1]
