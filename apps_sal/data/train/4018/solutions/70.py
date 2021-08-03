import re


def isDigit(str):
    return bool(re.match('^([-]?\d+\.\d+|\d+|-0)$', str))
