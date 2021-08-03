import re


def replace_dots(s):
    if s == '':
        return ''
    if '.' not in s:
        return 'no dots'
    return re.sub(r"\.", "-", s)
