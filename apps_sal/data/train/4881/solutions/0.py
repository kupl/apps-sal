import re


def camelize(s):
    return ''.join([w.capitalize() for w in re.split('\\W|_', s)])
