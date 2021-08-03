import re


def replace_exclamation(s):
    return re.sub('(?i)[aeiou]', '!', s)
