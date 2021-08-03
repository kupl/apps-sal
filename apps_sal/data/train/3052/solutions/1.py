import re


def remove(s):
    return re.sub(r'!+(?!!*$)', '', s)
