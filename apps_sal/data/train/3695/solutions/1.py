import re


def repeat_adjacent(s):
    return sum((len(set(i[0])) > 1 for i in re.findall('((([a-z])\\3+){2,})', s)))
