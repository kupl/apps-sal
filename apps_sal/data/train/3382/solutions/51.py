import re


def lowercase_count(strng):
    return len(''.join(re.findall(r'([a-z]+)', strng))) if re.search(r'([a-z]+)', strng) else 0
