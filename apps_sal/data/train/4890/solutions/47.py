def find_difference(a, b):
    s1 = a[0] * a[1] * a[2]
    s = b[0] * b[1] * b[2]
    return abs(s - s1)
