def scramble(s1, s2):
    char_count_s1 = {c: s1.count(c) for c in set(s1)}
    char_count_s2 = {c: s2.count(c) for c in set(s2)}
    for c in char_count_s2:
        if c not in char_count_s1:
            return False
        elif char_count_s1[c] < char_count_s2[c]:
            return False
    return True
