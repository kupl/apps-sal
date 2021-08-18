def scramble(s1, s2):
    for letter in 'abcdefghijklmnopqrstuwvxyz':
        if s1.count(letter) < s2.count(letter):
            return False
    return True
