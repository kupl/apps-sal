import re


def run_length_encoding(s):
    ls = re.finditer('(.)\\1*', s)
    t = []
    for i in ls:
        t.append([i.end() - i.start(), i.group()[0]])
    return t
