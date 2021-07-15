import re


def toUnderScore(name):
    return re.sub(r"(?<=[^^_])([A-Z]|\d+)", r"_\1", name)
