import re


def replace_dots(str=''):
    return re.sub('[.]', '-', str)
