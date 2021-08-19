import re


def apparently(s):
    return re.sub('(and\\b|but\\b)( apparently\\b)?', '\\1 apparently', s)
