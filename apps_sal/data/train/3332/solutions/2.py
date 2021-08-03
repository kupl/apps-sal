import re


def autocorrect(input):
    return re.sub(r'(?i)\b(you+|u)\b', 'your sister', input)
