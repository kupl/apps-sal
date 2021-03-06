import re
DERIVATE = re.compile('([+-]?)(\\d*)x\\^?(\\d*)')


def derivative(eq):
    rawDerivate = ''.join(('{}{}x^{}'.format(sign, int(coef or '1') * int(exp or '1'), int(exp or '1') - 1) for (sign, coef, exp) in DERIVATE.findall(eq)))
    derivate = re.sub('x\\^0|\\^1\\b', '', rawDerivate)
    return derivate or '0'
