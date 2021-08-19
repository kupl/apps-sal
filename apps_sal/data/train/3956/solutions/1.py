import re


def sort_string(s):
    sortedChr = iter(sorted(re.sub('[^a-zA-Z]', '', s), key=str.lower))
    return re.sub('[a-zA-Z]', lambda m: next(sortedChr), s)
