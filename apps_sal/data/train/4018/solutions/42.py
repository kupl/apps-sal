import re


def isDigit(string):
    return re.fullmatch('\\-{0,1}\\d+(\\.\\d+){0,1}', string) != None
