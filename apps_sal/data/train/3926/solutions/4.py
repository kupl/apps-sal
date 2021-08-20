def check_root(string):
    try:
        (a, b, c, d) = (int(d) for d in string.split(','))
    except ValueError:
        return 'incorrect input'
    if not a * d + 2 == b * c:
        return 'not consecutive'
    perfect = a * b * c * d + 1
    return '{}, {}'.format(perfect, int(perfect ** 0.5))
