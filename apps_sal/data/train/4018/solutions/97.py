import re


def isDigit(string):
    return False if re.match('^[-+]?([0-9]+(\\.[0-9]+)?|\\.[0-9]+)$', string.strip()) is None else True
