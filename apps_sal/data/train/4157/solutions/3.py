import re

BRACES = '\(\)|{}|\[\]'

def group_check(s):
    while re.search(BRACES, s):
        s = re.sub(BRACES, '', s)
    return s == ''
