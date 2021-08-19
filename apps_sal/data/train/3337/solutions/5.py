import re


def bracket_buster(s):
    return re.findall('\\[(.*?)\\]', s) if isinstance(s, str) else 'Take a seat on the bench.'
