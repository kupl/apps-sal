def derive(coefficient, exponent):
    x = []
    y = str(coefficient * exponent)
    x.append(y)
    x.append("x")
    x.append("^")
    z = str(exponent - 1)
    x.append(z)
    return ''.join(x)
