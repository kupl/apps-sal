def longest(s1, s2):
    distinct = set(s1 + s2)
    distinctSorted = sorted(distinct)
    return ''.join(distinctSorted)
