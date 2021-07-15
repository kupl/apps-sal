import re


def my_parse_int(string):
    return int(''.join([x for x in string if x.isdigit()])) if re.match(r'\s*\d+\s*$', string) else 'NaN'
