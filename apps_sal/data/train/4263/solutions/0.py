import re


def apparently(string):
    return re.sub('(?<=\\b(and|but)\\b(?! apparently\\b))', ' apparently', string)
