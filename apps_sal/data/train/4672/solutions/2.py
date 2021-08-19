import re


def AlphaNum_NumAlpha(string):
    return ''.join((chr(int(e) + 96) if e.isdigit() else str(ord(e) - 96) for e in re.split('([a-z])', string) if e))
