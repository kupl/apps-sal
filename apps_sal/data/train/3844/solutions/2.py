from numpy.polynomial import polynomial as P


def poly_from_roots(r):
    return P.polyfromroots(r).tolist()
