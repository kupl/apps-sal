import re


def to_integer(s):
    if re.match('\\A[+-]?(\\d+|0b[01]+|0o[0-7]+|0x[0-9a-fA-F]+)\\Z', s):
        return int(s, 10 if s[1:].isdigit() else 0)
