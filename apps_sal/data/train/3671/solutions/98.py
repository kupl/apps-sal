import re


def problem(a):
    if re.match('\\d', str(a)):
        return a * 50 + 6
    else:
        return 'Error'
