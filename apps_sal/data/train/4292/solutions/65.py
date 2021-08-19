import re


def string_clean(s):
    s = re.sub('[0-9]', '', s)
    return s
