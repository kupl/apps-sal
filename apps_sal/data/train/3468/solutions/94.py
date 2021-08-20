def scramble(s1, s2):
    (st1, st2) = (set(s1), set(s2))
    if not st2.issubset(st1):
        return False
    elif not all(map(lambda char: s1.count(char) >= s2.count(char), st2)):
        return False
    else:
        return True
