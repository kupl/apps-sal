import re


def string_clean(s):
    k = re.sub('\\d', '', s)
    return k
