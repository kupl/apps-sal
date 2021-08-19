import re


def has_subpattern(s):
    return re.search('^(.+?)\\1{1,}$', s) != None
