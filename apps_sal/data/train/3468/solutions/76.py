def scramble(s1, s2):
    s1_dict = dict()
    s2_dict = dict()

    s2_set = set(s2)

    for c in s2_set:
        s2_dict[c] = s2.count(c)
        s1_dict[c] = s1.count(c)

    for c in s2_set:  
        if c not in s1_dict or s2_dict[c] > s1_dict[c]: 
            return False

    return True
