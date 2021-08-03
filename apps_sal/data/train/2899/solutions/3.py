import re


def bin_str(s):
    return len(re.findall(r'0+|1+', s.lstrip('0')))
