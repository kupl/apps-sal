def longest(s1, s2):
    return ''.join(sorted(list(dict.fromkeys(s1 + s2))))
