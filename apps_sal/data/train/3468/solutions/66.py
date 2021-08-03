def scramble(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    for letter in set2:
        if letter not in set1:
            return False
        if s1.count(letter) < s2.count(letter):
            return False
    else:
        return True
