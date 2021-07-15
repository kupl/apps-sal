from numpy.linalg import solve

def solve_eq(eq):
    (*eq1, d1), (*eq2, d2), (*eq3, d3) = eq
    return list(map(round, solve([eq1, eq2, eq3], [d1, d2, d3])))
