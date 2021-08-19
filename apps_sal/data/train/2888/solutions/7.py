import re


def remove(s):
    return re.sub('(?<=\\w)!+(?=\\s|$)', '', s)
