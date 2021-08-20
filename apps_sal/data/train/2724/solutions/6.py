import re


def kebabize(string):
    return re.sub('(?!^)([A-Z])', '-\\1', re.sub('\\d', '', string)).lower()
