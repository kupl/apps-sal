import re


def meeting(s):
    return ''.join(sorted(re.sub('(\\w+):(\\w+);?', '(\\2, \\1);', s.upper()).split(';')))
