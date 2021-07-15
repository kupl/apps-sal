def find_difference(a, b):
    vol_a = a[0] * a[1] * a[2]
    vol_b = b[0] * b[1] * b[2]
    return vol_a - vol_b if vol_a > vol_b else vol_b - vol_a
