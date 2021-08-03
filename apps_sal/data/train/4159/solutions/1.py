from numpy import polymul


def poly_multiply(p1, p2):
    res = list(polymul(p1, p2))
    return res if any(res) else []
