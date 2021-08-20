import re


def trump_detector(ts):
    x = re.findall('([aeiou])(\\1*)', ts, re.I)
    y = [len(i[1]) for i in x]
    return round(sum(y) / len(y), 2)
