def scramble(s1, s2):
    s = list(set(s2))
    for i in s:
        if s1.count(i) < s2.count(i):
            return False
    return True
