from itertools import zip_longest


def poly_multiply(a, b):
    return [sum(i) for i in zip_longest(*[[0] * i + [j * k for k in a] for (i, j) in enumerate(b)], fillvalue=0)] if a else []
