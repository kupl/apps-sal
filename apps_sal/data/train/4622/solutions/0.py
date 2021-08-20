import re


def double_check(str):
    return bool(re.search('(.)\\1', str.lower()))
