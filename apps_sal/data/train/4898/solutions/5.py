def digit_all(x):
    if not isinstance(x, str):
        return 'Invalid input !'
    return ''.join(filter(str.isdigit, x))
