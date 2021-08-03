import re


def camelize(str_):
    return ''.join(x.capitalize() for x in re.split(r'[\W_]', str_))
