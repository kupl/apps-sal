import re


def kebabize(string):
    return re.sub(r'(?!^)([A-Z])', r'-\1', re.sub('\d', '', string)).lower()
