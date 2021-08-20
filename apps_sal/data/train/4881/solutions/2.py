import re


def camelize(s):
    return ''.join(map(str.capitalize, re.findall('[a-zA-Z0-9]+', s)))
