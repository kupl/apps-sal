def integrate(coefficient, exponent):
    NewExp = exponent + 1
    NewCoe = int(coefficient / NewExp)
    integral = str(NewCoe) + 'x^' + str(NewExp)
    return integral
