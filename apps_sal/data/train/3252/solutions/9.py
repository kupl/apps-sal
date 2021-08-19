import re


def is_letter(s):
    return bool(re.fullmatch('[a-zA-Z]', s))
