def scramble(s1, s2):
    for c in "qwertyuiopasdfghjklzxcvbnm":
        if s1.count(c) < s2.count(c): return False
    return True

