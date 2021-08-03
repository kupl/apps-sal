import re


def is_letter(s):
    return bool(re.match(r'^[a-z]$', re.escape(s), re.I))
