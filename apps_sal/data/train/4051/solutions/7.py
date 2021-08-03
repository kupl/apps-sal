import re


def toUnderScore(name):
    return re.sub(r'(?<!^)(?<!_)(\d+|[A-Z][a-z]*)', r'_\1', name)
