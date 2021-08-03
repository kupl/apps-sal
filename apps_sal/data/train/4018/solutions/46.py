import re


def isDigit(string):
    print(string)
    return bool(re.match(r'^-?\d*\.?\d+$', string))
