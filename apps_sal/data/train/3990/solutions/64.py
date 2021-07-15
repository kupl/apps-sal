def derive(c, e):
    if e > 2 :
        code = e-1
    else:
        code = e
    return str(c*e) + "x^" + str(code)
