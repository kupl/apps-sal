import re

FORBIDDENS = set("a the on at of upon in as".split())

def word_count(s):
    return sum(m[0] not in FORBIDDENS for m in re.finditer(r'[a-z]+',s.lower()))
