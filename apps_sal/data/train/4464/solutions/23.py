import re


def feast(beast, dish):
    return re.sub(r'\B(.*)\B', '', beast) == re.sub(r'\B(.*)\B', '', dish)
