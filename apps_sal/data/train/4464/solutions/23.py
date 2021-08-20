import re


def feast(beast, dish):
    return re.sub('\\B(.*)\\B', '', beast) == re.sub('\\B(.*)\\B', '', dish)
