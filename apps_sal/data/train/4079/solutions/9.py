import re


def encode(string):
    return re.sub('[a-z]', lambda m: str(ord(m.group()) - ord('a') + 1), string.lower())
