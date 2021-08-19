import re


def encode(s):
    return re.sub('[a-zA-Z]', lambda m: str((ord(m.group()) + 1) % 2), s)
