import re


def replace_dots(string):
    if string == '':
        return ''
    else:
        return string.replace('.', '-') if '.' in list(string) else 'no dots'
