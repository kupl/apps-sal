import re


def string_clean(s):
    o = []
    nonolist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for x in list(s):
        if x not in nonolist:
            o.append(x)
    return ''.join(o)
