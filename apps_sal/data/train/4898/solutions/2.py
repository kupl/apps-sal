def digit_all(x):
    if type(x).__name__ != 'str':
        return 'Invalid input !'
    return ''.join(c for c in x if c in '123456789')
