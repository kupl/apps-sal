def integrate(coefficient, exponent):
    i_co = coefficient / (exponent + 1)
    i_ex = exponent + 1
    return str(int(i_co)) + 'x^' + str(int(i_ex))
