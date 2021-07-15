def scramble(s1, s2):
    return all([s1.count(l2) >= s2.count(l2) for l2 in set(s2)])
