import numpy as np


def solve_eq(eq):
    m = np.array(eq)
    return np.linalg.solve(m[:, :3], m[:, 3]).round().astype(int).tolist()
