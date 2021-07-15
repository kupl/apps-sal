def is_substitution_cipher(s1, s2):
    return len(set(s1)) == len(set(s2)) == len(set(zip(s1, s2)))
