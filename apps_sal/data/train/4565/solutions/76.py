import re


def replace_dots(str):
    return "no dots" if set(str) == {'-'} else re.sub(r"\.", "-", str)
