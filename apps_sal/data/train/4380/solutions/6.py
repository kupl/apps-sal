import re


def remove_chars(s):
    return re.sub('(?i)[^a-z ]', '', s)
