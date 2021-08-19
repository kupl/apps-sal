import re


def to_acronym(s):
    return ''.join(re.findall('\\b(\\w)', s)).upper()
