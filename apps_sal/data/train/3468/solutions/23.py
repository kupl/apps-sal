def scramble(s1, s2):
    return all([s2.count(c) <= s1.count(c) for c in set(s2)])
