import re


def clean_string(s):
    while '#' in s:
        s = re.sub('.?#', '', s, count=1)
    return s
