import re


def encode(s):
    return re.sub('\\S+', lambda m: m.group()[-2::-1] + m.group()[-1], s)
