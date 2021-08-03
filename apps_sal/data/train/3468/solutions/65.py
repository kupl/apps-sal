def scramble(s1, s2):
    d1 = {}
    for i in set(s1):
        d1[i] = s1.count(i)
    for i in set(s2):
        try:
            if s2.count(i) > d1[i]:
                return False
        except:
            return False
    return True
