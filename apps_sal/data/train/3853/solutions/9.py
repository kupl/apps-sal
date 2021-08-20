from itertools import cycle


def numeric_formatter(template, num='1234567890'):
    digits = cycle(num)
    return ''.join((next(digits) if char.isalpha() else char for char in template))
