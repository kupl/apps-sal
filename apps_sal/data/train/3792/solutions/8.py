import re


def slogans(p, r):
    if not r:
        return 0
    return 1 + slogans(p, r.replace(re.search(r'.+?(.+)\s\1.*', ' '.join([p, r])).group(1), '', 1))
