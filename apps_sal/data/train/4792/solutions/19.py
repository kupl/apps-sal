import re

def parse_float(string):
    return float(string) if type(string) == str and re.match(r'\d+\.\d+$', string) else None
