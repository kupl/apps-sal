import re


def pig_it(text):
    return re.sub('([a-z])([a-z]*)', '\\2\\1ay', text, flags=re.I)
