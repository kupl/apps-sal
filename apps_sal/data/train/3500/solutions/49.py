import re


def remove_exclamation_marks(str):
    return ''.join(re.findall('\\w|\\s|[,]', str))
