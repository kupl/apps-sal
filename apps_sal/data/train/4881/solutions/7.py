import re


def camelize(str_):
    return ''.join([i.capitalize() for i in re.findall('[A-Za-z0-9]*', str_)])
