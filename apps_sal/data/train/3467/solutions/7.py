def integrate(coeff, index):
    return '{}x^{}'.format(coeff/(index + 1), index + 1).replace('.0x', 'x')
