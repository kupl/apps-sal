import re


def whitespace(st):
    return len(re.findall('\\s', st)) == len(st)
