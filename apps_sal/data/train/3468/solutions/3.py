def scramble(s1, s2):
    return all(s1.count(x) >= s2.count(x) for x in set(s2))
