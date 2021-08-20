import re


def str2int(s):
    return int(s + '1' * (not s[-1:].isdigit()))


def monomial(args):
    (c, p) = map(str2int, args)
    return '%+d' % (c * p) + 'x' * (p > 1) + '^%d' % (p - 1) * (p > 2)


def derivative(eq):
    return ''.join(map(monomial, re.findall('(-?\\d*)x\\^?(\\d*)', eq))).lstrip('+') or '0'
