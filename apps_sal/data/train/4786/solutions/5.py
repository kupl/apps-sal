def poly_derivative(p):
    result = []
    for (i, n) in enumerate(p[1:], start=1):
        result.append(n * i)
    return result
