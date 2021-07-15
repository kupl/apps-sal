def scramble(s1, s2):
    for l in set(s2):
        if l not in s1 or s1.count(l) < s2.count(l):
            return False
    return True
