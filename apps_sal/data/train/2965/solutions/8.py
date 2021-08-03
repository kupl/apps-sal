import numpy as np


def solve_eq(eq):
    return [i[0] for i in np.linalg.solve(np.reshape([x for x in (y[:-1] for y in eq)], (3, 3)), np.reshape([x for x in (y[-1] for y in eq)], (3, 1))).round().astype(int)]
