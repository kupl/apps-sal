def find_difference(v, w):
    a, b, c, d, e, f = v[0], v[1], v[2], w[0], w[1], w[2]
    return a * b * c - d * e * f if a * b * c > d * e * f else d * e * f - a * b * c
