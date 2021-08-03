import re


def domino_reaction(s):
    return re.sub('^\|+', lambda m: '/' * len(m.group()), s, count=1)
