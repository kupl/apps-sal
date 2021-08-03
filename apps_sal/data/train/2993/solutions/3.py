from itertools import zip_longest


def poly_add(*polys):
    return [sum(coeffs) for coeffs in zip_longest(*polys, fillvalue=0)]
