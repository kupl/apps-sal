import re


def doubles(s):
    while len(re.sub('([a-z])\\1', '', s)) != len(s):
        s = re.sub('([a-z])\\1', '', s)
    return s
