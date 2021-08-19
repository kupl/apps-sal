import re


def string_parse(s):
    if not isinstance(s, str):
        return 'Please enter a valid string'
    for l in set(s):
        s = re.sub('(%s%s)(%s+)' % (l, l, l), '\\1[\\2]', s)
    return s
