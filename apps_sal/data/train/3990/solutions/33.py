def derive(coefficient, exponent):
    if exponent == 2:
        mult = coefficient * exponent
        mult = str(mult)
        return mult + 'x'
    else:
        multiply = coefficient * exponent
        n = exponent - 1
        n = str(n)
        multiply = str(multiply)
        return multiply + 'x' + '^' + n
