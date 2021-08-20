import re


def autocorrect(input):
    return re.sub('(?i)\\b(you+|u)\\b', 'your sister', input)
