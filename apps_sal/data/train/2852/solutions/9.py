import re


def find_longest(s):
    regex = '\\(a*\\)'
    while re.search(regex, s):
        s = re.sub(regex, lambda x: 'a' * len(x.group()), s)
    r = map(len, re.findall('a+', s))
    return max(r, default=0)
