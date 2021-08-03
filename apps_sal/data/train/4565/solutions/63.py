import re


def replace_dots(str):
    new = re.sub(r"\.", "-", str)
    return new
