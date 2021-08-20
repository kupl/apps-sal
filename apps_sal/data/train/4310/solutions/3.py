import re


def swap(st):
    return re.sub('[aeiou]', lambda m: m.group(0).upper(), st)
