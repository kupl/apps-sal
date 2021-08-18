def poly_derivative(p):

    der = []

    for i in range(1, len(p)):
        der.append(i * p[i])

    return der
