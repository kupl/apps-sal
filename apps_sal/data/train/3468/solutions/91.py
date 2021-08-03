def scramble(s1, s2):
    from collections import Counter
    c1 = Counter(s1)
    c2 = Counter(s2)
    for key, val in c2.items():
        if key not in c1.keys():
            return False
        else:
            if val > c1[key]:
                return False
    return True
