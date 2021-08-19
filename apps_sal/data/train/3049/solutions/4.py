import re


def textin(st):
    return re.sub('t[wo]?o', '2', st, flags=re.IGNORECASE)
