def get_derivative(s):
    if 'x' not in s: return '0'
    if '^' not in s: return s.replace('x', '')
    a, b = [int(n) for n in s.split('x^')]
    a *= b
    b -= 1
    if b == 1: return '{}x'.format(a)
    return '{}x^{}'.format(a, b)
