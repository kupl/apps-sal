import re


def parse_float(string):
    return float(string) if type(string) == str and re.match('\\d+\\.\\d+$', string) else None
