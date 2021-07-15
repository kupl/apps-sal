def scramble(s1, s2):
    for c in set(s2):
        if s2.count(c) > s1.count(c):
            return False
    return True
