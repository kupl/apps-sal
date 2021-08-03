def scramble(s1, s2):
    list = []
    for letter in s2:
        if letter in list:
            continue
        else:
            list.append(letter)
        if s2.count(letter) <= s1.count(letter):
            pass
        else:
            return False
    return True
