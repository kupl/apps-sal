import re


def replace_dots(s):
    if len(s) == 0:
        return ''
    return re.sub('\\.', '-', s) if '.' in s else 'no dots'
