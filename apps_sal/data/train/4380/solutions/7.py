import re


def remove_chars(s):
    return re.sub(r'(?i)[^a-z ]', "", s)
