def integrate(c, e):
    return '{}x^{}'.format(c / (e + 1), e + 1).replace('.0x', 'x')
