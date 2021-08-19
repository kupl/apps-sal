import re


def bin_str(s):
    return len(re.findall('(?:1+)|(?:0+)', s.lstrip('0')))
