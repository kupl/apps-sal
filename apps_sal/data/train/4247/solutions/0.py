import re
pattern = re.compile('o(.*?)d(.*?)d')


def odd(s):
    n = 0
    while pattern.search(s):
        n += 1
        s = pattern.sub('\\1\\2', s, count=1)
    return n
