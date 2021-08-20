def digit_all(x):
    if isinstance(x, str):
        return ''.join((x for x in x if x.isnumeric()))
    else:
        return 'Invalid input !'
