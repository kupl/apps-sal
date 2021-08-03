def derive(coefficient, exponent):
    a = [str((coefficient * exponent)), str((exponent - 1))]

    return (a[0] + "x^" + a[1])
