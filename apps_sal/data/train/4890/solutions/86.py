def find_difference(a, b):
    a1 = a[0] * a[1] * a[2]
    b1 = b[0] * b[1] * b[2]
    m = max(a1, b1)
    m1 = min(a1, b1)
    return m - m1
