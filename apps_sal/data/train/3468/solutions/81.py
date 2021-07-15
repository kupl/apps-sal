def scramble(s1, s2):
    fr = set(s1)
    sc = set(s2)
    for i in sc:
        if i not in fr:
            return False
        elif i in fr:
            if s1.count(i) < s2.count(i):
                return False            
    return True

