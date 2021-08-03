def derive(coefficient, exponent):
    base = str(coefficient * exponent)
    exp = str(exponent - 1)
    return ("%sx^%s" % (base, exp))
