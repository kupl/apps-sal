import re

def sort_string(s):
    sortedChr = iter(sorted(re.sub(r'[^a-zA-Z]', '', s), key=str.lower))
    return re.sub(r'[a-zA-Z]', lambda m: next(sortedChr), s)
