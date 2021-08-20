import re


def isDigit(string):
    return True if re.match('^-?\\d*\\.?\\d+$', string) else False
