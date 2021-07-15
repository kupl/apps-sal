def is_substitution_cipher(s1, s2):
    plain, cipher = {}, {}
    for a, b in zip(s1, s2):
        if plain.setdefault(a, b) != b or cipher.setdefault(b, a) != a:
            return False
    return True
