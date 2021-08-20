import re


def fat_fingers(s):
    return re.sub('[aA](.*?)(a|A|$)', lambda m: m[1].swapcase(), s)
