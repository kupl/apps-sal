import re


def isDigit(string):
    print(string)
    return bool(re.match('^-?\\d*\\.?\\d+$', string))
