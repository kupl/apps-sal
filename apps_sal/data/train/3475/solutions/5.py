import re


def to_integer(string):
    result = re.compile(r'^(\+|-)?(0b[01]+|0o[0-7]+|0x(\d|[abcdefABCDEF])+|\d+)\Z').match(string)
    if not result:
        return None
    return convert_to_number(result.string)


def convert_to_number(string):
    base_dict = {'0x': 16, '0b': 2, '0o': 8}
    for key, value in base_dict.items():
        if string.find(key) != -1:
            return int(string, value)
    return int(string)
