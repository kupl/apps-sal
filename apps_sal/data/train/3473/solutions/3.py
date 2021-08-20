from itertools import groupby


def doubles(s):
    new_s = ''.join((char * (len(tuple(group)) % 2) for (char, group) in groupby(s)))
    return new_s if len(new_s) == len(s) else doubles(new_s)
