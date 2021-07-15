_RESULTS = {
    'goodpresent': lambda y: ''.join(chr(ord(c) + y) for c in 'goodpresent'),
    'crap': lambda y: 'acpr',
    'empty': lambda y: 'empty',
    'bang': lambda y: str(sum(ord(c) - y for c in 'bang')),
    'badpresent': lambda y: 'Take this back!',
    'dog': lambda y: 'pass out from excitement {} times'.format(y)
}

present = lambda x, y: _RESULTS[x](y)
