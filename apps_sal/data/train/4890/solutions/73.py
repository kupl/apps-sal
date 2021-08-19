def find_difference(a, b):
    (x, y, z) = (a[0], a[1], a[2])
    (r, s, t) = (b[0], b[1], b[2])
    volume1 = x * y * z
    volume2 = r * s * t
    difference = volume1 - volume2
    if volume1 > volume2:
        return difference
    else:
        return -difference
