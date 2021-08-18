def scramble(s1, s2):
    Mot = "".join(dict.fromkeys(s2))
    for i in range(len(Mot)):
        if s1.count(Mot[i]) < s2.count(Mot[i]):
            return False

    return True
