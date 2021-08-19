import re


def to_integer(string):
    s = re.match('^([+-]?((0x[0-9A-Fa-f]+)|(0b[01]+)|(0o[0-7]+))?(?(2)$|[0-9]+$))', string)
    if s == None or s.group(1) != string:
        return None
    return int(string, 0 if s.group(2) else 10)
