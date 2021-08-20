def derive(c, e):
    c = c * e
    e -= 1
    return str(c) + 'x^' + str(e)
