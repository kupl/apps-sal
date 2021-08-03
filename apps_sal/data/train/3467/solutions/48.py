def integrate(coefficient, exponent):
    new_ex = exponent + 1
    new_str = str(int(coefficient / new_ex)) + 'x^' + str(new_ex)
    return ''.join(new_str)
