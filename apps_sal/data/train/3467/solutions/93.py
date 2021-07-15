def integrate(coefficient, exponent):
    end = exponent + 1
    begin = coefficient // end
    return str(begin) + 'x^' + str(end)
