import re


def double_check(s):
    return re.search('(?i)(.)\\1', s) != None
