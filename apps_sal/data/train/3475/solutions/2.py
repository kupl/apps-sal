import re


def to_integer(s):
    decimal = re.compile('^[-+]?\\d+$')
    binary = re.compile('^[-+]?0b[01]+$')
    hexadecimal = re.compile('^[-+]?0x[0-9A-Fa-f]+$')
    octal = re.compile('^[-+]?0o[0-7]+$')
    return next((int(s, [10, 0][j != 0]) for (j, i) in enumerate([decimal, binary, hexadecimal, octal]) if re.search(i, s) and '\n' not in s), None)
