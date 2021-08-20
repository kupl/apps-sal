import re


def replace_dots(str):
    if str == '':
        return re.sub('.', '-', str)
    return str.replace('.', '-')
