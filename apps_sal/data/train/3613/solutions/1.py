def f(s1, s2):
    d = {}
    for a, b in zip(s1, s2):
        if (a in d and d[a] != b):
            return False
        d[a] = b
    return True

def is_substitution_cipher(s1, s2):
    return f(s1, s2) and f(s2, s1)
