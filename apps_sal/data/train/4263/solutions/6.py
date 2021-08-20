import re


def apparently(s):
    return re.sub('\\b(and|but)(?:\\b)(?! apparently\\b)', lambda m: m.group() + ' apparently', s)
