import re


def is_letter(s):
    return bool(re.match('^[a-z]$', re.escape(s), re.I))
