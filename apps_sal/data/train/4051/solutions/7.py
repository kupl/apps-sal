import re


def toUnderScore(name):
    return re.sub('(?<!^)(?<!_)(\\d+|[A-Z][a-z]*)', '_\\1', name)
