from numpy import poly
def poly_from_roots(r): return list(reversed(poly(r))) if len(r) else [1]
