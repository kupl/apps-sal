import re


def is_valid(idn):
    pattern = '^[a-zA-z_\\$]+[\\w\\$]*$'
    return bool(re.match(pattern, idn))
