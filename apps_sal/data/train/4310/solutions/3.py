import re


def swap(st):
    return re.sub(r'[aeiou]', lambda m: m.group(0).upper(), st)
