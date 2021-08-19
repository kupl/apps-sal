def scramble(s1, s2):
    s2_dict = {}
    for c in set(s2):
        s2_dict[c] = s2.count(c)
    output = True
    for c in sorted(s2_dict, key=s2_dict.get, reverse=True):
        s2_count = s2_dict[c]
        if s2_count > s1.count(c):
            output = False
            break
    return output
