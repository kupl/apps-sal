import re


def is_letter(s):
    return bool(re.fullmatch(r"[a-zA-Z]", s))
