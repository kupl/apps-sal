def dollar_to_speech(value):
    (d, c) = map(int, value[1:].split('.'))
    if d < 0:
        return 'No negative numbers are allowed!'
    if d == 0 == c:
        return '0 dollars.'
    s = ''
    if d > 0:
        s += '{} dollar{}{}'.format(d, 's' * (d > 1), ' and ' * (c > 0))
    if c > 0:
        s += '{} cent{}'.format(c, 's' * (c > 1))
    return s + '.'
