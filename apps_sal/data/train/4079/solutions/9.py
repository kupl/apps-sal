import re


def encode(string):
    return re.sub(r'[a-z]', lambda m: str(ord(m.group()) - ord('a') + 1), string.lower())
