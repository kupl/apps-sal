import re


def reverser(sentence):
    return ''.join((w[::-1] if ' ' not in w else w for w in re.findall('(?:\\w+)|(?:\\s+)', sentence)))
