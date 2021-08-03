import numpy as np


def solve_eq(eq):
    a = np.array([arr[:3] for arr in eq])
    b = np.array([arr[-1] for arr in eq])
    return [round(x) for x in np.linalg.solve(a, b)]
