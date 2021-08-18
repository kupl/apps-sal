import re


def remove_exclamation_marks(str):
    return "".join(re.findall(r"\w|\s|[,]", str))
