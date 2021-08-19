import re


def remove(s):
    return re.sub('(?<=\\w)!+(?=\\W)*', '', s)
