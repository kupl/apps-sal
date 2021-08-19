# return the derivative of the polynomial.
def poly_derivative(p):
    return [(i + 1) * m for i, m in enumerate(p[1:])]
