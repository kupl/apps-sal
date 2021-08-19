def dollar_to_speech(value):
    x = value.lstrip('$')
    if float(x) < 0:
        return 'No negative numbers are allowed!'
    (dollars, cents) = map(int, x.split('.'))
    speech = []
    if cents:
        speech.append('{} cent{}'.format(cents, 's' if cents != 1 else ''))
    if dollars or not speech:
        speech.insert(0, '{} dollar{}'.format(dollars, 's' if dollars != 1 else ''))
    return ' and '.join(speech) + '.'
