from numpy import poly
poly_from_roots=lambda r:list(reversed(poly(r))) if len(r) else [1]
