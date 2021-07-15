import re

def has_subpattern(string):
    return bool(re.match(r'(.+)\1+$', string))
