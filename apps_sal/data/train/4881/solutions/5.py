import re


def camelize(str_):
    return ''.join((x.capitalize() for x in re.split('[\\W_]', str_)))
