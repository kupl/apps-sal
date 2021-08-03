def digit_all(x):
    return filter(str.isdigit, x) if isinstance(x, str) else 'Invalid input !'
