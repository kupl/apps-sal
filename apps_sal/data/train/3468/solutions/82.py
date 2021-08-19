def scramble(s1, s2):
    if None in (s1, s2):
        return False
    passed = []
    for letter in s2:
        if letter in passed:
            continue
        if letter not in s1 or s2.count(letter) > s1.count(letter):
            return False
        passed.append(letter)
    else:
        return True
