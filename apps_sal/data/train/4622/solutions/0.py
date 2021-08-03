import re


def double_check(str):
    return bool(re.search(r"(.)\1", str.lower()))
