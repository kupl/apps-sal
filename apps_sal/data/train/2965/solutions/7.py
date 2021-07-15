from numpy import array as a, matrix as m

def solve_eq(eq):
    return [round(i[0]) for i in a(m([i[:3] for i in eq]).I * m([i[3] for i in eq]).T)]
