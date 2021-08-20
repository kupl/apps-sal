from re import match


def isDigit(string):
    return bool(match('^[-+]?\\d+\\.?\\d*?$', string))
