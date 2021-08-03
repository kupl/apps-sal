def scramble(s1, s2):
    list_chr = tuple(set(s2))
    for i in list_chr:
        if s1.count(i) < s2.count(i):
            return False
    return True
