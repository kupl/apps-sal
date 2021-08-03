def polynomialize(roots):
    coeffs = [1]
    for root in roots:
        coeffs = [1] + [coeffs[i] + coeffs[i - 1] * -root for i in range(1, len(coeffs))] + [-root * coeffs[-1]]
    coeffs = [d for d in list(enumerate(coeffs[::-1]))[::-1] if d[1] != 0]
    r = ['{:+0d}x^{}'.format(d[1], d[0]) for d in coeffs if d[0] > 1]
    r += ['{:+0d}x'.format(d[1]) for d in coeffs if d[0] == 1]
    r += ['{:+0d}'.format(d[1]) for d in coeffs if d[0] == 0]
    f = ' '.join(r).replace('+1x', '+x').replace('-1x', '-x').replace('-', '- ').replace('+', '+ ').lstrip('+').strip(' ')
    return f + ' = 0'
