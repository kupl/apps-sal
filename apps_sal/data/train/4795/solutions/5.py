import re


def flesch_kincaid(s):
    w = len(s.split())
    return round(0.39 * w / len(re.split('[!.?]', s)[:-1]) + 11.8 * len(re.findall('[aeiou]+', s, re.I)) / w - 15.59, 2)
