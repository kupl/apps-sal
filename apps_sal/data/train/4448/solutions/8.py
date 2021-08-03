def get_derivative(str):
    if 'x' not in str:
        return '0'
    if '^' not in str:
        return str[:-1]
    a, b = str.split('^')
    na = int(a[:-1]) * int(b)
    b = int(b) - 1
    if b == 1:
        return '{}x'.format(na)
    else:
        return '{}x^{}'.format(na, b)
