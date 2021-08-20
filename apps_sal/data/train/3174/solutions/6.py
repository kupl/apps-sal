import re
nomial = re.compile('(?P<sign>[\\+-]?)(?P<coef>[0-9]*)(?P<x>[a-z]?)\\^?(?P<exp>[0-9]*)')


def derive(eq):
    if not eq:
        return ''
    m = nomial.match(eq)
    c = int(m.group('coef') or '1')
    exp = int(m.group('exp') or '1')
    if not m.group('x'):
        r = ''
    elif not m.group('exp'):
        r = m.group('sign') + str(c)
    elif m.group('exp') == '2':
        r = m.group('sign') + str(c * 2) + m.group('x')
    else:
        r = m.group('sign') + str(c * exp) + m.group('x') + '^' + str(exp - 1)
    return r + derive(eq[m.end():])


def derivative(eq):
    return derive(eq) or '0'
