def scramble(s1, s2):
    clean = ''
    boolean = []
    for i in s2:
        if i not in clean:
            clean = clean + i
    for i in clean:
        if s2.count(i) > s1.count(i):
            return False
    return True
