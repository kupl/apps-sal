import re


def isDigit(string):
    return True if re.match(r'^-?\d*\.?\d+$', string) else False
