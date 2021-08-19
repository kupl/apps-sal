import re


def autocorrect(input):
    rgx = '\\b([Yy]ou+|u)\\b'
    return re.sub(rgx, 'your sister', input)
