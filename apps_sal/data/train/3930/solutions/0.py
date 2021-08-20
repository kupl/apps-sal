def dollar_to_speech(value):
    if '-' in value:
        return 'No negative numbers are allowed!'
    (d, c) = (int(n) for n in value.replace('$', '').split('.'))
    dollars = '{} dollar{}'.format(str(d), 's' if d != 1 else '') if d or not c else ''
    link = ' and ' if d and c else ''
    cents = '{} cent{}'.format(str(c), 's' if c != 1 else '') if c else ''
    return '{}{}{}.'.format(dollars, link, cents)
