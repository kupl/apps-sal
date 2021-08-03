import numpy


def poly_from_roots(r): return list(reversed(numpy.poly(tuple(r)))) if len(r) > 0 else [1]
