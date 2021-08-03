import re


def remove(s):
    return re.sub(r"(?<=\w)!+(?=\W)*", "", s)
