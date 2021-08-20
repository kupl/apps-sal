import re


def string_clean(s):
    result = re.sub('\\d', '', s)
    return result
    '\n    Function will return the cleaned string\n    '
