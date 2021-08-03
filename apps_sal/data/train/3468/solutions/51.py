def scramble(s1, s2):
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if s2.count(letter) <= s1.count(letter):
            continue
        else:
            return False
    return True
