import re


def alphabetized(s):
    return ''.join(sorted(re.sub(r'[^A-Za-z]', '', s), key=str.lower))
