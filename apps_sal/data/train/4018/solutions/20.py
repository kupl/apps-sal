import re


def isDigit(s):
    return re.match('^(-?)(([0-9]+\\.[0-9]+)|([0-9]+))$', s) is not None
