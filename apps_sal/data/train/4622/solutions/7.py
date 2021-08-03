import re


def double_check(strng):
    return bool(re.search(r"(.)\1", strng, re.IGNORECASE))
