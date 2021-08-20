import re


def find(s):
    h1 = re.findall('!+\\?+', s)
    h2 = re.findall('\\?+!+', s)
    return max(h1 + h2, key=lambda x: (len(x), -s.find(x)), default='')
