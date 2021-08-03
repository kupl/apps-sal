import re


def replace_dots(s):
    if '.' in s:

        return s.replace(".", "-")
    else:
        return s
