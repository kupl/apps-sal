def find_difference(a, b):
    aa = a[0] * a[1] * a[2]
    bb = b[0] * b[1] * b[2]
    return max(aa, bb) - min(aa, bb)
