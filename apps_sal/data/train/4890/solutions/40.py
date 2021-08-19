def find_difference(a, b):
    return a[0] * a[1] * a[2] - b[0] * b[1] * b[2] if a[0] * a[1] * a[2] - b[0] * b[1] * b[2] > 0 else b[0] * b[1] * b[2] - a[0] * a[1] * a[2]
