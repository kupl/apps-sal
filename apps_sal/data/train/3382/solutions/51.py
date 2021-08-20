import re


def lowercase_count(strng):
    return len(''.join(re.findall('([a-z]+)', strng))) if re.search('([a-z]+)', strng) else 0
