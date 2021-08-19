import re


def sursurungal(txt):
    txt = re.sub('\\b2\\s(\\S+)s', '2 bu\\1', txt)
    txt = re.sub('\\b([3-9])\\s(\\S+)s', '\\1 \\2zo', txt)
    return re.sub('(\\d+\\d)\\s(\\S+)s', '\\1 ga\\2ga', txt)
