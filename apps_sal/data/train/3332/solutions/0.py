import re


def autocorrect(input):
    return re.sub('(?i)\\b(u|you+)\\b', 'your sister', input)
