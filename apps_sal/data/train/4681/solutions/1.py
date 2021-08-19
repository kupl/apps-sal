import re


def alphabetized(s):
    return ''.join(sorted(re.sub('[^A-Za-z]', '', s), key=str.lower))
