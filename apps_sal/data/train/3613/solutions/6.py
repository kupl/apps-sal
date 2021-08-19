def is_substitution_cipher(s1, s2):
    return s2 == s1.translate(str.maketrans(s1, s2)) and s1 == s2.translate(str.maketrans(s2, s1))
