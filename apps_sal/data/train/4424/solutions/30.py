import numpy as np


def expression_matter(a, b, c):
    A = a * b * c
    B = a * (b + c)
    C = a * b + c
    D = a + b + c
    E = a + b * c
    F = (a + b) * c
    R = np.array([A, B, C, D, E, F])
    return R.max()
