import re


def is_letter(s):
    return bool(re.fullmatch('[A-Za-z]', s))
