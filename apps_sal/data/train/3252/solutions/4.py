import re


def is_letter(s):
    return re.match('(?i)[a-z]\\Z', s) is not None
