def scramble(s1, s2):
    for el in set(s2):
        if not s1.count(el) >= s2.count(el):
            return False
    return True
