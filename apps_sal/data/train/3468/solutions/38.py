def scramble(s1, s2):
    a = [s1.count(chr(i)) - s2.count(chr(i)) for i in range(97, 123)]
    for i in a:
        if i < 0:
            return False
    return True
