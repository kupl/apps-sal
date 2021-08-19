def integrate(a, b):
    return ''.join((str(i) for i in [a // (b + 1), 'x^', b + 1]))
