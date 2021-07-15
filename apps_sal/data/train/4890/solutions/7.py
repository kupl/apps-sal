def find_difference(a, b):
    a_volume = a[0] * a[1] * a[2]
    b_volume = b[0] * b[1] * b[2]
    return abs(a_volume - b_volume)
