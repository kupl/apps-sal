import re


def apparently(stg):
    return re.sub('\\b(and|but)\\b(?! apparently\\b)', '\\1 apparently', stg)
