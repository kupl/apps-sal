import re


def is_letter(s):
    return re.match(r'(?i)[a-z]\Z', s) is not None
