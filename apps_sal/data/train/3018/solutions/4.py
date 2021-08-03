import re


def word_count(s):
    words = re.findall(r'[a-z]+', s, re.I)
    return sum(not re.match(r'(a|the|on|at|of|upon|in|as)$', w, re.I) for w in words)
