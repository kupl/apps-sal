import re


def remove(stg):
    return ' '.join((re.sub('(!*)([^!]+)(!*)', equalize, word) for word in stg.split()))


def equalize(match):
    (before, word, after) = match.groups()
    shortest = min(before, after, key=len)
    return f'{shortest}{word}{shortest}'
