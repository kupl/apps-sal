import re


def double_check(strng):
    return True if re.findall('(.)\\1', strng.lower()) else False
