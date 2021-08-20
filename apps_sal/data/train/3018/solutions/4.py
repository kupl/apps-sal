import re


def word_count(s):
    words = re.findall('[a-z]+', s, re.I)
    return sum((not re.match('(a|the|on|at|of|upon|in|as)$', w, re.I) for w in words))
