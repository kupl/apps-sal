import re


def remove(s):
    return re.sub('\\b!+', '', s)
