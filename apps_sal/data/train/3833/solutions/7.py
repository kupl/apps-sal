def longest(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    return ''.join(sorted(set1 | set2))
