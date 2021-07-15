def scramble(s1, s2):
    for char in list(set(list(s2))):
        if char not in s1: return False
        if s2.count(char) > s1.count(char): return False
    return True
