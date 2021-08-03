def get_derivative(f):
    a, b = map(int, (f + '^%d' % ('x' in f)).replace('x', '').split('^')[:2])
    return {0: '0', 1: '%d' % a, 2: '%dx' % (a * b)}.get(b, '%dx^%d' % (a * b, b - 1))
