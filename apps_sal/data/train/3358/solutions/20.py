import re


def correct(string):
    return re.sub('(\\d)', lambda x: {'5': 'S', '0': 'O', '1': 'I'}[x.group()], string)
