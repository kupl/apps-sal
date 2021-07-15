import numpy as np
def solve_eq(eq):
    [p, q, r] = eq
    a = np.array([p[:-1], q[:-1], r[:-1]])
    b = np.array([p[-1], q[-1], r[-1]])
    return list(map(round,np.linalg.solve(a, b).tolist()))

