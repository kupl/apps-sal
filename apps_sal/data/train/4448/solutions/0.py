def get_derivative(s):
    if '^' in s:
        (f, t) = map(int, s.split('x^'))
        return '{}x'.format(f * t) if t == 2 else '{}x^{}'.format(f * t, t - 1)
    elif 'x' in s:
        return s[:-1]
    else:
        return '0'
