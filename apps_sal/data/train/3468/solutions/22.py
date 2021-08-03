def scramble(s1, s2):
    for i in "abcdefghijklmnopqrstuvwxyz":
        if s1.count(i) < s2.count(i):
            return False
    return True
