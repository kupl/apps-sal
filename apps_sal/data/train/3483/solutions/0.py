import re


def string_parse(string):
    return re.sub('(.)\\1(\\1+)', '\\1\\1[\\2]', string) if isinstance(string, str) else 'Please enter a valid string'
