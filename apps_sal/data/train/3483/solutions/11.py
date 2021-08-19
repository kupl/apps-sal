import re


def string_parse(s):
    return re.sub('((.)\\2*)', lambda x: f'{2 * x[2]}[{x[1][:len(x[1]) - 2]}]' if len(x[1]) > 2 else x[1], s) if isinstance(s, str) else 'Please enter a valid string'
