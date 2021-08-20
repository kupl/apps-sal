import re


def toUnderScore(name):
    return re.sub('(?<=[^^_])([A-Z]|\\d+)', '_\\1', name)
