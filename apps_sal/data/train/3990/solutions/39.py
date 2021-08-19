def derive(coefficient, exponent):
    sub = exponent - 1
    multi = coefficient * exponent
    coffie = str(sub)
    ex = str(multi)
    result = ex + 'x^' + coffie
    return result
