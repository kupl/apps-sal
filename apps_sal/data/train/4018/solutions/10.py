import re


def isDigit(string):
    return bool(re.search('^-?[\\d\\.]+$', string))
