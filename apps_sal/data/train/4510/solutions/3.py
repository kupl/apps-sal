import re


def to_underscore(string):
    return re.sub("(?<=.)(?=[A-Z])", "_", str(string)).lower()
