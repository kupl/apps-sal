import re


def double_check(strng):
    return True if re.findall(r"(.)\1", strng.lower()) else False
