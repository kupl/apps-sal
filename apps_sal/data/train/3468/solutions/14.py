def scramble(s1, s2):
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = []
    for char in a:
        if s1.count(char) >= s2.count(char):
            b.append(True)
        else:
            b.append(False)
    if len(set(b)) <= 1:
        return True
    else:
        return False
