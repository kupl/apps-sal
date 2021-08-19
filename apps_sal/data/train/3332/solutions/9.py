import re


def autocorrect(s):
    return re.sub('(?i)\\b(u|you+)\\b', 'your sister', s)
