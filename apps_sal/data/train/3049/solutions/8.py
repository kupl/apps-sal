import re


def textin(st):
    obj = re.compile('(two|too|to)', re.I)
    return obj.sub('2', st)
