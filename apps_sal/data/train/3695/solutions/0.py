from re import findall


def repeat_adjacent(s):
    return len(findall('((.)\\2+(?!\\2)){2,}', s))
