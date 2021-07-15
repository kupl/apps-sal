def poly_derivative(p):
    return [el * idx for idx, el in enumerate(p) if idx > 0]
