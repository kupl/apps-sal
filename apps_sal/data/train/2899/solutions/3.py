import re


def bin_str(s):
    return len(re.findall('0+|1+', s.lstrip('0')))
