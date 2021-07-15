from itertools import cycle

def numeric_formatter(template, data='1234567890'):
    data = cycle(data)
    return ''.join(next(data) if c.isalpha() else c for c in template)
