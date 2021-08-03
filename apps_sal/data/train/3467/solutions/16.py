def integrate(c, e):
    coefficient = str(c / (e + 1))
    return coefficient.rstrip('0').rstrip('.') + 'x^' + str(e + 1)
