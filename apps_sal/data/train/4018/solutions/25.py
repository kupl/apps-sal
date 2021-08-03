import re


def isDigit(string):
    return bool(re.match("-?\d+(\.\d+)?$", string))
