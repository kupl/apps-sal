import re

def bears(x,s):
    matches = re.findall('(B8|8B)', s)
    return [''.join(matches), len(matches)>=x]
