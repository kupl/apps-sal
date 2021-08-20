def find_difference(a, b):
    a = a[0] * a[1] * a[2]
    b = b[0] * b[1] * b[2]
    if a > b:
        d = a - b
        return d
    else:
        d = b - a
        return d
