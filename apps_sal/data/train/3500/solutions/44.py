import re


def remove_exclamation_marks(s):
    res = re.sub('!', '', s)
    return res
