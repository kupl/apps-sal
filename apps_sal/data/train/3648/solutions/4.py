import re

def summy(s):
    return sum(map(int, re.split(r'[^\d]+', s)))
