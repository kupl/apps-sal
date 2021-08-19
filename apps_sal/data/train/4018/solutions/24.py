import re


def isDigit(string):
    return True if re.search('(^-*[0-9\\.]+$)', string) else False
