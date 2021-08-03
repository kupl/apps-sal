def integrate(c, exp):
    if c / (exp + 1) % 1 == 0:
        return '{:g}x^{}'.format(c / (exp + 1), exp + 1)
    else:
        return '{}x^{}'.format(c / (exp + 1), exp + 1)
