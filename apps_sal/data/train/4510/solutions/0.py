import re


def to_underscore(string):
    return re.sub('(.)([A-Z])', '\\1_\\2', str(string)).lower()
