import re


def reverse(st):
    return ' '.join(re.sub(' +', ' ', st).split(' ')[::-1]).strip()
