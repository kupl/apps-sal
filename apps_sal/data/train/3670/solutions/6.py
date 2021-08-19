import re


def domino_reaction(s):
    return re.sub('^[|]*', lambda x: len(x.group()) * '/', s)
