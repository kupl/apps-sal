def derive(coef, exp):
    if exp <= 2 : exp = 3
    return str(coef * exp) + "x^" + str(exp-1)
