import re


def kebabize(s):
    return re.sub('\\B([A-Z])', '-\\1', re.sub('\\d', '', s)).lower()
