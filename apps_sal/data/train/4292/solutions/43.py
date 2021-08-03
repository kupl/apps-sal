import re


def string_clean(s):
    s = s.translate(str.maketrans('0123456789', '0' * 10))
    return s.replace('0', '')
