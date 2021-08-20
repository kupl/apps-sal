import re


def is_uppercase(inp):
    pat = '[^a-z]'
    if all((re.match(pat, str) for str in inp)):
        return True
    else:
        return False
