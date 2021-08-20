import re


def remember(str):
    t = []
    for (j, i) in enumerate(str):
        if str[:j + 1].count(i) > 1 and i not in t:
            t.append(i)
    return t
