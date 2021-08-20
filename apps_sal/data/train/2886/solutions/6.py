import re


def find(s):
    return max(re.findall('\\!+\\?+', s) + re.findall('\\?+\\!+', s), key=lambda x: (len(x), -s.index(x)), default='')
