import re


def no_space(s):
    return re.sub('\\s', '', s)
