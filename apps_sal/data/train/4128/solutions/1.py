import re


def bears(x, s):
    r = re.findall(r'8B|B8', s)
    return [''.join(r), len(r) >= x]
